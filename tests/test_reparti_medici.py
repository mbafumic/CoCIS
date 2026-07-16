"""Anagrafica organizzativa: Reparto e Medico.

Verifica la seconda gerarchia polimorfica del progetto (`Dipendente` → `Medico`),
la M:M reparti↔dipendenti, i self-riferimenti e — soprattutto — che i
FK-placeholder accumulati dalle slice precedenti ora navighino davvero.
"""

from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.dipendente import Dipendente
from app.models.disciplina import Disciplina
from app.models.medico import Medico
from app.models.paziente import Paziente
from app.models.prenotazione import Prenotazione
from app.models.presidio_osp import PresidioOsp
from app.models.reparto import Reparto


def test_medico_e_sottotipo_polimorfico_di_dipendente(db_session: Session) -> None:
    dipendente = Dipendente(cognome="Rossi", nome="Mario")
    medico = Medico(cognome="Bianchi", nome="Anna", chirurgo=True, codice_regionale="MI12345")
    db_session.add_all([dipendente, medico])
    db_session.flush()

    assert dipendente.tipo_personale == "dipendente"
    assert medico.tipo_personale == "medico"

    # interrogando la base si ottiene l'istanza del sottotipo giusto
    db_session.expire_all()
    tutti = db_session.scalars(select(Dipendente).order_by(Dipendente.cognome)).all()
    per_tipo = {d.cognome: d for d in tutti}
    assert isinstance(per_tipo["Bianchi"], Medico)
    assert not isinstance(per_tipo["Rossi"], Medico)

    # e la query sul sottotipo filtra solo i medici
    medici = db_session.scalars(select(Medico)).all()
    assert [m.cognome for m in medici] == ["Bianchi"]


def test_medico_firma_referti_calcolata(db_session: Session) -> None:
    medico = Medico(cognome="Bianchi", nome="Anna", codice_regionale="MI12345")
    db_session.add(medico)
    db_session.flush()
    assert medico.firma_referti == "Bianchi Anna - MI12345"
    assert medico.nominativo == "Bianchi Anna"


def test_reparto_presidio_e_self_ref_magazzino(db_session: Session) -> None:
    presidio = PresidioOsp(presidio="PO Centrale")
    magazzino = Reparto(reparto="Magazzino centrale", tipo="Supporto", presidio=presidio)
    degenza = Reparto(
        reparto="Cardiochirurgia",
        tipo="Degenza",
        presidio=presidio,
        letti_accreditati=20,
        reparto_mag=magazzino,
    )
    db_session.add_all([presidio, magazzino, degenza])
    db_session.flush()

    assert degenza.reparto_mag.reparto == "Magazzino centrale"
    assert {r.reparto for r in presidio.reparti} == {"Magazzino centrale", "Cardiochirurgia"}


def test_medico_tutor_spec_self_ref(db_session: Session) -> None:
    tutor = Medico(cognome="Verdi", nome="Luca")
    specializzando = Medico(
        cognome="Neri", nome="Sara", specializzando=True, tutor_spec=tutor, anno_corso="II"
    )
    db_session.add_all([tutor, specializzando])
    db_session.flush()

    assert specializzando.tutor_spec.cognome == "Verdi"


def test_m2m_reparti_dipendenti(db_session: Session) -> None:
    cardio = Reparto(reparto="Cardiochirurgia")
    terapia = Reparto(reparto="Terapia intensiva")
    medico = Medico(cognome="Bianchi", nome="Anna")
    medico.reparti = [cardio, terapia]
    db_session.add_all([cardio, terapia, medico])
    db_session.flush()

    # navigabile in entrambe le direzioni
    assert {r.reparto for r in medico.reparti} == {"Cardiochirurgia", "Terapia intensiva"}
    assert medico in cardio.dipendenti


def test_placeholder_sciolti_reparto_predefinito_e_disciplina(db_session: Session) -> None:
    """Prima erano colonne Integer senza FK: ora navigano davvero."""
    reparto = Reparto(reparto="Cardiochirurgia")
    responsabile = Medico(cognome="Bianchi", nome="Anna")
    dipendente = Dipendente(cognome="Rossi", nome="Mario", reparto_predefinito=reparto)
    disciplina = Disciplina(
        disciplina="Cardiochirurgia",
        codice="08",
        reparto_degenza=reparto,
        responsabile=responsabile,
    )
    db_session.add_all([reparto, responsabile, dipendente, disciplina])
    db_session.flush()

    assert dipendente.reparto_predefinito.reparto == "Cardiochirurgia"
    assert disciplina.reparto_degenza.id == reparto.id
    assert disciplina.responsabile.nominativo == "Bianchi Anna"


def test_placeholder_sciolti_specialisti_prenotazione(db_session: Session) -> None:
    paziente = Paziente(
        nome="Giovanni",
        cognome="Russo",
        data_nascita=date(1970, 1, 1),
        codice_fiscale="RSSGVN70A01H501Q",
    )
    chirurgo = Medico(cognome="Bianchi", nome="Anna", chirurgo=True)
    internista = Medico(cognome="Verdi", nome="Luca")
    db_session.add_all([paziente, chirurgo, internista])
    db_session.flush()

    prenotazione = Prenotazione(
        paziente_id=paziente.id,
        tipo_contatto="prenotazione",
        data_apertura=date(2026, 7, 1),
        data=date(2026, 7, 1),
        specialista_chirurgo=chirurgo,
        specialista_medico=internista,
        tutor=chirurgo,
    )
    db_session.add(prenotazione)
    db_session.flush()

    # tre FK distinte verso la stessa tabella medici
    assert prenotazione.specialista_chirurgo.cognome == "Bianchi"
    assert prenotazione.specialista_medico.cognome == "Verdi"
    assert prenotazione.tutor.id == chirurgo.id


def test_presidio_direttore_sanitario_navigabile_senza_fk(db_session: Session) -> None:
    """Il ciclo presidi_osp->medici->dipendenti->presidi_osp impedisce una FK a DB
    (come nel legacy), ma la relationship resta navigabile."""
    direttore = Medico(cognome="Bianchi", nome="Anna")
    db_session.add(direttore)
    db_session.flush()

    presidio = PresidioOsp(presidio="PO Centrale", direttore_sanitario_id=direttore.id)
    db_session.add(presidio)
    db_session.flush()
    db_session.expire_all()

    ricaricato = db_session.get(PresidioOsp, presidio.id)
    assert ricaricato.direttore_sanitario is not None
    assert ricaricato.direttore_sanitario.cognome == "Bianchi"
