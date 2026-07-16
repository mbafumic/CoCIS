"""create pazienti, contatti_pz, ricoveri

Revision ID: d8c87d4e55d9
Revises:
Create Date: 2026-07-13 16:28:04.250696

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d8c87d4e55d9"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # --- tabelle lookup senza dipendenze ---
    op.create_table(
        "regioni",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("regione", sa.String(length=25), nullable=False),
        sa.Column("codice", sa.String(length=3), nullable=True),
        sa.Column("ordine_stampa", sa.Integer(), nullable=True),
    )

    op.create_table(
        "gruppi_sanguigni",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("gruppo", sa.String(length=10), nullable=False),
        sa.Column("transcodifica", sa.String(length=100), nullable=True),
    )

    op.create_table(
        "titoli",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("titolo", sa.String(length=10), nullable=False),
    )

    op.create_table(
        "tipi_dipendente",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("tipo", sa.String(length=30), nullable=False),
    )

    op.create_table(
        "rapporti_dipendenza",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("rapporto", sa.String(length=40), nullable=False),
    )

    op.create_table(
        "gradi_urgenza",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("grado_urgenza", sa.String(length=30), nullable=False),
        sa.Column("colore", sa.Integer(), nullable=True),
    )

    op.create_table(
        "modalita_accesso",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("modalita", sa.String(length=50), nullable=False),
    )

    op.create_table(
        "provenienze",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("provenienza", sa.String(length=70), nullable=False),
        sa.Column("anno_inizio_validita", sa.Integer(), nullable=True),
        sa.Column("anno_fine_validita", sa.Integer(), nullable=True),
    )

    op.create_table(
        "diagnosi",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("descrizione", sa.String(length=60), nullable=True),
        sa.Column("abbreviazione", sa.String(length=15), nullable=True),
        sa.Column("icd9_cm_id", sa.Integer(), nullable=True),
    )

    op.create_table(
        "stati_civili",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("stato_civile", sa.String(length=20), nullable=False),
    )

    op.create_table(
        "professioni",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("professione", sa.String(length=30), nullable=False),
    )

    op.create_table(
        "posizioni_professionali",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("posizione", sa.String(length=30), nullable=False),
    )

    op.create_table(
        "tipi_documento",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("tipo_documento", sa.String(length=20), nullable=False),
    )

    op.create_table(
        "livelli_istruzione",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("livello_istruzione", sa.String(length=40), nullable=False),
    )

    op.create_table(
        "categorie_paziente",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("categoria", sa.String(length=100), nullable=False),
    )

    op.create_table(
        "stati",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("stato", sa.String(length=30), nullable=False),
        sa.Column("codice_istat", sa.String(length=3), nullable=True),
        sa.Column("nazionalita", sa.String(length=20), nullable=True),
        sa.Column("codice_iso", sa.String(length=3), nullable=True),
        sa.Column("comunitario", sa.Boolean(), nullable=True),
    )

    # --- tabelle lookup con dipendenze semplici ---
    op.create_table(
        "comuni",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("comune", sa.String(length=35), nullable=False),
        sa.Column("istat", sa.String(length=6), nullable=True),
        sa.Column("provincia", sa.String(length=2), nullable=True),
        sa.Column("regione_id", sa.Integer(), sa.ForeignKey("regioni.id"), nullable=True),
        sa.Column("prefisso", sa.String(length=5), nullable=True),
        sa.Column("cap", sa.String(length=5), nullable=True),
        sa.Column("cod_fisco", sa.String(length=4), nullable=True),
        sa.Column("abitanti", sa.Integer(), nullable=True),
    )

    op.create_table(
        "asp",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("azienda", sa.String(length=3), nullable=True),
        sa.Column("denominazione", sa.String(length=50), nullable=True),
        sa.Column("indirizzo", sa.String(length=50), nullable=True),
        sa.Column("cap", sa.String(length=6), nullable=True),
        sa.Column("citta_id", sa.Integer(), sa.ForeignKey("comuni.id"), nullable=True),
        sa.Column("regione_id", sa.Integer(), sa.ForeignKey("regioni.id"), nullable=True),
        sa.Column("anno", sa.Integer(), nullable=True),
        sa.Column("partita_iva", sa.String(length=11), nullable=True),
    )

    op.create_table(
        "medici_esterni",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("cognome", sa.String(length=30), nullable=True),
        sa.Column("nome", sa.String(length=30), nullable=True),
        sa.Column("indirizzo", sa.String(length=80), nullable=True),
        sa.Column("telefono", sa.String(length=30), nullable=True),
        sa.Column("cellulare", sa.String(length=20), nullable=True),
        sa.Column("citta_id", sa.Integer(), sa.ForeignKey("comuni.id"), nullable=True),
        sa.Column("codice_regionale", sa.String(length=16), nullable=True),
        sa.Column("n_empam", sa.String(length=10), nullable=True),
        sa.Column("asp_id", sa.Integer(), sa.ForeignKey("asp.id"), nullable=True),
        sa.Column("specializzazione", sa.String(length=50), nullable=True),
        sa.Column("codice_fiscale", sa.String(length=16), nullable=True),
        sa.Column("codice_altro_sistema", sa.Integer(), nullable=True),
    )

    op.create_table(
        "presidi_osp",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("presidio", sa.String(length=100), nullable=True),
        sa.Column("comune_id", sa.Integer(), sa.ForeignKey("comuni.id"), nullable=True),
        sa.Column("indirizzo", sa.String(length=60), nullable=True),
        sa.Column("cap", sa.String(length=6), nullable=True),
        sa.Column("tel", sa.String(length=20), nullable=True),
        sa.Column("fax", sa.String(length=20), nullable=True),
        sa.Column("email", sa.String(length=50), nullable=True),
        sa.Column("asp_id", sa.Integer(), sa.ForeignKey("asp.id"), nullable=True),
        sa.Column("header", sa.Text(), nullable=True),
        sa.Column("footer", sa.Text(), nullable=True),
        sa.Column("header_fattura", sa.Text(), nullable=True),
        sa.Column("header_clinico", sa.Text(), nullable=True),
        sa.Column("smtp", sa.String(length=50), nullable=True),
        sa.Column("mail_host", sa.String(length=50), nullable=True),
        sa.Column("smtp_port", sa.Integer(), nullable=True),
        sa.Column("home_page", sa.LargeBinary(), nullable=True),
        sa.Column("direttore_sanitario_id", sa.Integer(), nullable=True),
        sa.Column("responsabile_dipartimento_id", sa.Integer(), nullable=True),
    )

    # dipendenti dipende da comuni, presidi_osp, titoli, tipi_dipendente, rapporti_dipendenza
    op.create_table(
        "dipendenti",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("cognome", sa.String(length=30), nullable=False),
        sa.Column("nome", sa.String(length=30), nullable=False),
        sa.Column("data_nascita", sa.Date(), nullable=True),
        sa.Column("sesso", sa.String(length=1), nullable=True),
        sa.Column("comune_nascita_id", sa.Integer(), sa.ForeignKey("comuni.id"), nullable=True),
        sa.Column("codice_fiscale", sa.String(length=16), nullable=True),
        sa.Column("partita_iva", sa.String(length=11), nullable=True),
        sa.Column("comune_residenza_id", sa.Integer(), sa.ForeignKey("comuni.id"), nullable=True),
        sa.Column("indirizzo", sa.String(length=80), nullable=True),
        sa.Column("telefono", sa.String(length=20), nullable=True),
        sa.Column("cellulare", sa.String(length=20), nullable=True),
        sa.Column(
            "rapporto_dipendenza_id",
            sa.Integer(),
            sa.ForeignKey("rapporti_dipendenza.id"),
            nullable=True,
        ),
        sa.Column("data_inizio_rapporto", sa.Date(), nullable=True),
        sa.Column("data_fine_rapporto", sa.Date(), nullable=True),
        sa.Column("badge", sa.String(length=20), nullable=True),
        sa.Column("sigla", sa.String(length=6), nullable=True),
        sa.Column("titolo_id", sa.Integer(), sa.ForeignKey("titoli.id"), nullable=True),
        sa.Column(
            "tipo_dipendente_id", sa.Integer(), sa.ForeignKey("tipi_dipendente.id"), nullable=True
        ),
        sa.Column("presidio_id", sa.Integer(), sa.ForeignKey("presidi_osp.id"), nullable=True),
        sa.Column("reparto_predefinito_id", sa.Integer(), nullable=True),
        sa.Column("email", sa.String(length=60), nullable=True),
        sa.Column("utente_email", sa.String(length=60), nullable=True),
        sa.Column("password_email", sa.String(length=30), nullable=True),
        sa.Column("pec", sa.String(length=70), nullable=True),
        sa.Column("elenco_globale", sa.Boolean(), nullable=True),
        sa.Column("documentix_sezione", sa.Boolean(), nullable=True),
        sa.Column("mostra_ricoveri", sa.Boolean(), nullable=True),
        sa.Column("mostra_sala_operatoria", sa.Boolean(), nullable=True),
        sa.Column("richiesta_emocomponenti", sa.Boolean(), nullable=True),
        sa.Column("segreteria", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column(
            "no_intestazione_referti_amb",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),
        sa.Column("presenza_omonimo", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("avvisato", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("firma_digitalizzata", sa.LargeBinary(), nullable=True),
        sa.Column("tipo_firma", sa.String(length=20), nullable=True),
        sa.Column("stato_fse", sa.String(length=20), nullable=True),
        sa.Column("password_changed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("tipo_rilevazione_inventario", sa.String(length=10), nullable=True),
        sa.Column("pin_web", sa.String(length=10), nullable=True),
        sa.Column("nodo_startup", sa.String(length=100), nullable=True),
        sa.Column("codice_esterno", sa.Integer(), nullable=True),
        sa.Column("id_esterno", sa.Integer(), nullable=True),
        sa.Column("avviso", sa.Text(), nullable=True),
    )

    # discipline dipende da dipendenti (responsabile)
    op.create_table(
        "discipline",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("codice", sa.String(length=2), nullable=True),
        sa.Column("disciplina", sa.String(length=50), nullable=True),
        sa.Column("attiva", sa.Boolean(), nullable=True),
        sa.Column("trasferimento_interno", sa.Boolean(), nullable=True),
        sa.Column("standard_procedure", sa.String(length=100), nullable=True),
        sa.Column("gg_terapia_fino_sosp", sa.Integer(), nullable=True),
        sa.Column("allegati_cc", sa.Boolean(), nullable=True),
        sa.Column("responsabile_id", sa.Integer(), sa.ForeignKey("dipendenti.id"), nullable=True),
        sa.Column("reparto_degenza_id", sa.Integer(), nullable=True),
    )

    # --- anagrafica principale ---
    op.create_table(
        "pazienti",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nome", sa.String(length=100), nullable=False),
        sa.Column("cognome", sa.String(length=100), nullable=False),
        sa.Column("data_nascita", sa.Date(), nullable=False),
        sa.Column("codice_fiscale", sa.String(length=16), nullable=False),
        sa.Column("sesso", sa.String(length=1), nullable=True),
        sa.Column("eta", sa.String(length=9), nullable=True),
        sa.Column("luogo_nascita_id", sa.Integer(), sa.ForeignKey("comuni.id"), nullable=True),
        sa.Column(
            "gruppo_sanguigno_id",
            sa.Integer(),
            sa.ForeignKey("gruppi_sanguigni.id"),
            nullable=True,
        ),
        sa.Column("deceduto", sa.Boolean(), nullable=True),
        sa.Column("testimone_di_geova", sa.Boolean(), nullable=True),
        sa.Column("telefoni_paziente", sa.String(length=200), nullable=True),
        sa.Column("telefoni_parenti", sa.String(length=200), nullable=True),
        sa.Column("consenso_tratt_pers", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("consenso_dossier", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("download_referti", sa.String(length=20), nullable=True),
        sa.Column("codice_esterno", sa.Integer(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )
    op.create_index("ix_pazienti_codice_fiscale", "pazienti", ["codice_fiscale"], unique=True)

    op.create_table(
        "contatti_pz",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("paziente_id", sa.Integer(), sa.ForeignKey("pazienti.id"), nullable=False),
        sa.Column("tipo_contatto", sa.String(length=50), nullable=False),
        sa.Column("data_apertura", sa.Date(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("indirizzo", sa.String(length=50), nullable=True),
        sa.Column("cap", sa.String(length=6), nullable=True),
        sa.Column("comune_residenza_id", sa.Integer(), sa.ForeignKey("comuni.id"), nullable=True),
        sa.Column("stato_residenza_id", sa.Integer(), sa.ForeignKey("stati.id"), nullable=True),
        sa.Column("cittadinanza_id", sa.Integer(), sa.ForeignKey("stati.id"), nullable=True),
        sa.Column("stato_civile_id", sa.Integer(), sa.ForeignKey("stati_civili.id"), nullable=True),
        sa.Column("professione_id", sa.Integer(), sa.ForeignKey("professioni.id"), nullable=True),
        sa.Column(
            "posizione_professionale_id",
            sa.Integer(),
            sa.ForeignKey("posizioni_professionali.id"),
            nullable=True,
        ),
        sa.Column(
            "livello_istruzione_id",
            sa.Integer(),
            sa.ForeignKey("livelli_istruzione.id"),
            nullable=True,
        ),
        sa.Column(
            "categoria_paziente_id",
            sa.Integer(),
            sa.ForeignKey("categorie_paziente.id"),
            nullable=True,
        ),
        sa.Column(
            "tipo_documento_id", sa.Integer(), sa.ForeignKey("tipi_documento.id"), nullable=True
        ),
        sa.Column("documento", sa.String(length=20), nullable=True),
        sa.Column("data_rilascio", sa.Date(), nullable=True),
        sa.Column("ente_rilascio", sa.String(length=40), nullable=True),
        sa.Column(
            "medico_curante_id", sa.Integer(), sa.ForeignKey("medici_esterni.id"), nullable=True
        ),
        sa.Column("asp_residenza_id", sa.Integer(), sa.ForeignKey("asp.id"), nullable=True),
        sa.Column("presidio_id", sa.Integer(), sa.ForeignKey("presidi_osp.id"), nullable=True),
        sa.Column("operatore_id", sa.Integer(), sa.ForeignKey("dipendenti.id"), nullable=True),
        sa.Column("tessera_team", sa.String(length=30), nullable=True),
        sa.Column("peso", sa.Float(), nullable=True),
        sa.Column("altezza", sa.Integer(), nullable=True),
        sa.Column("num_ist_team", sa.String(length=50), nullable=True),
        sa.Column("ente_rilascio_eni_stp", sa.String(length=50), nullable=True),
        sa.Column("data_rilascio_eni_stp", sa.Date(), nullable=True),
        sa.Column("data_scadenza_team_eni_stp", sa.Date(), nullable=True),
        sa.Column("diniego_fse", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column(
            "nega_presenza_allergie", sa.Boolean(), nullable=False, server_default=sa.false()
        ),
        sa.Column(
            "nega_presenza_patologie", sa.Boolean(), nullable=False, server_default=sa.false()
        ),
        sa.Column(
            "nega_presenza_patologie_infettive",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),
        sa.Column("last_update", sa.DateTime(timezone=True), nullable=True),
        sa.Column("pc_last_update", sa.String(length=40), nullable=True),
    )
    op.create_index("ix_contatti_pz_paziente_id", "contatti_pz", ["paziente_id"])

    # --- sottotipi di contatti_pz: percorso ricovero ---
    op.create_table(
        "prenotazioni",
        sa.Column("id", sa.Integer(), sa.ForeignKey("contatti_pz.id"), primary_key=True),
        sa.Column("data", sa.Date(), nullable=True),
        sa.Column("regime_ricovero", sa.String(length=20), nullable=True),
        sa.Column("data_prevista_ricovero", sa.Date(), nullable=True),
        sa.Column("ora_ricovero", sa.DateTime(timezone=True), nullable=True),
        sa.Column("data_prev_pre_ric", sa.Date(), nullable=True),
        sa.Column("data_tampone", sa.Date(), nullable=True),
        sa.Column(
            "grado_urgenza_id", sa.Integer(), sa.ForeignKey("gradi_urgenza.id"), nullable=True
        ),
        sa.Column(
            "unita_funzionale_id", sa.Integer(), sa.ForeignKey("discipline.id"), nullable=True
        ),
        sa.Column(
            "diagnosi_ingresso_id", sa.Integer(), sa.ForeignKey("diagnosi.id"), nullable=True
        ),
        sa.Column(
            "modalita_accesso_id", sa.Integer(), sa.ForeignKey("modalita_accesso.id"), nullable=True
        ),
        sa.Column(
            "medico_inviante_id", sa.Integer(), sa.ForeignKey("medici_esterni.id"), nullable=True
        ),
        sa.Column("specialista_medico_id", sa.Integer(), nullable=True),
        sa.Column("specialista_chirurgo_id", sa.Integer(), nullable=True),
        sa.Column("tutor_id", sa.Integer(), nullable=True),
        sa.Column("note_amministrative", sa.String(length=250), nullable=True),
        sa.Column("note_cliniche", sa.String(length=255), nullable=True),
        sa.Column("classe_priorita", sa.String(length=1), nullable=True),
        sa.Column("motivo_dh", sa.String(length=20), nullable=True),
        sa.Column("stato", sa.String(length=20), nullable=True),
        sa.Column("bloccato", sa.Boolean(), nullable=True),
        sa.Column("data_blocco", sa.Date(), nullable=True),
        sa.Column("email", sa.String(length=60), nullable=True),
        sa.Column("camera_singola", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("data_avviso", sa.Date(), nullable=True),
        sa.Column("avvisato", sa.Boolean(), nullable=False, server_default=sa.false()),
    )

    op.create_table(
        "prericoveri",
        sa.Column("id", sa.Integer(), sa.ForeignKey("contatti_pz.id"), primary_key=True),
        sa.Column("regime_ricovero", sa.String(length=20), nullable=True),
        sa.Column(
            "disciplina_ricovero_id", sa.Integer(), sa.ForeignKey("discipline.id"), nullable=True
        ),
        sa.Column("data_inizio", sa.Date(), nullable=True),
        sa.Column("data_fine", sa.Date(), nullable=True),
        sa.Column("cartella_clinica", sa.Integer(), nullable=True),
        sa.Column(
            "modalita_accesso_id", sa.Integer(), sa.ForeignKey("modalita_accesso.id"), nullable=True
        ),
        sa.Column("scheda_e", sa.Boolean(), nullable=True),
        sa.Column("codice_impegnativa", sa.String(length=7), nullable=True),
        sa.Column("numero_impegnativa", sa.String(length=11), nullable=True),
        sa.Column("data_impegnativa", sa.Date(), nullable=True),
        sa.Column("provenienza_id", sa.Integer(), sa.ForeignKey("provenienze.id"), nullable=True),
        sa.Column(
            "diagnosi_ingresso_id", sa.Integer(), sa.ForeignKey("diagnosi.id"), nullable=True
        ),
        sa.Column(
            "medico_inviante_id", sa.Integer(), sa.ForeignKey("medici_esterni.id"), nullable=True
        ),
        sa.Column("prenotazione_id", sa.Integer(), sa.ForeignKey("prenotazioni.id"), nullable=True),
        sa.Column("locked_user_id", sa.Integer(), sa.ForeignKey("dipendenti.id"), nullable=True),
        sa.Column("specialista_medico_id", sa.Integer(), nullable=True),
        sa.Column("specialista_chirurgo_id", sa.Integer(), nullable=True),
        sa.Column("tutor_id", sa.Integer(), nullable=True),
        sa.Column("parente_id", sa.Integer(), nullable=True),
        sa.Column("note_amministrative", sa.String(length=250), nullable=True),
        sa.Column("note_cliniche", sa.String(length=250), nullable=True),
        sa.Column("computer", sa.String(length=50), nullable=True),
        sa.Column("anno_prericovero", sa.Integer(), nullable=True),
        sa.Column("mese_prericovero", sa.String(length=10), nullable=True),
    )
    op.create_index("ix_prericoveri_cartella_clinica", "prericoveri", ["cartella_clinica"])

    op.create_table(
        "ricoveri",
        sa.Column("id", sa.Integer(), sa.ForeignKey("contatti_pz.id"), primary_key=True),
        sa.Column("reparto", sa.String(length=100), nullable=False),
        sa.Column("data_ricovero", sa.Date(), nullable=False),
        sa.Column("data_dimissione", sa.Date(), nullable=True),
        sa.Column("stato", sa.String(length=20), nullable=False, server_default="aperto"),
        sa.Column("prenotazione_id", sa.Integer(), sa.ForeignKey("prenotazioni.id"), nullable=True),
        sa.Column("prericovero_id", sa.Integer(), sa.ForeignKey("prericoveri.id"), nullable=True),
    )

    op.create_table(
        "disdetta_prenotazione",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("motivo", sa.String(length=200), nullable=True),
        sa.Column(
            "prenotazione_id",
            sa.Integer(),
            sa.ForeignKey("prenotazioni.id"),
            nullable=True,
            unique=True,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("disdetta_prenotazione")
    op.drop_table("ricoveri")
    op.drop_index("ix_prericoveri_cartella_clinica", table_name="prericoveri")
    op.drop_table("prericoveri")
    op.drop_table("prenotazioni")
    op.drop_index("ix_contatti_pz_paziente_id", table_name="contatti_pz")
    op.drop_table("contatti_pz")
    op.drop_index("ix_pazienti_codice_fiscale", table_name="pazienti")
    op.drop_table("pazienti")
    op.drop_table("discipline")
    op.drop_table("dipendenti")
    op.drop_table("presidi_osp")
    op.drop_table("medici_esterni")
    op.drop_table("asp")
    op.drop_table("comuni")
    op.drop_table("diagnosi")
    op.drop_table("provenienze")
    op.drop_table("modalita_accesso")
    op.drop_table("gradi_urgenza")
    op.drop_table("rapporti_dipendenza")
    op.drop_table("tipi_dipendente")
    op.drop_table("titoli")
    op.drop_table("stati")
    op.drop_table("categorie_paziente")
    op.drop_table("livelli_istruzione")
    op.drop_table("tipi_documento")
    op.drop_table("posizioni_professionali")
    op.drop_table("professioni")
    op.drop_table("stati_civili")
    op.drop_table("gruppi_sanguigni")
    op.drop_table("regioni")
