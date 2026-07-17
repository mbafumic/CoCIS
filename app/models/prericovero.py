from datetime import date
from typing import TYPE_CHECKING, Literal

from sqlalchemy import Boolean, Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.contatto_pz import ContattoPz

if TYPE_CHECKING:
    from app.models.diagnosi import Diagnosi
    from app.models.dipendente import Dipendente
    from app.models.disciplina import Disciplina
    from app.models.medico import Medico
    from app.models.medico_esterno import MedicoEsterno
    from app.models.modalita_accesso import ModalitaAccesso
    from app.models.prenotazione import Prenotazione
    from app.models.provenienza import Provenienza
    from app.models.ricovero import Ricovero


class Prericovero(ContattoPz):
    """Prericovero: accesso per esami preliminari prima del ricovero.

    Sottotipo concreto di ContattoPz. Può nascere da una Prenotazione (link
    opzionale) e a sua volta sfociare in un Ricovero (FK sul Ricovero).

    Nel legacy la PK è composita `(OID, CartellaClinica)`: quirk XPO. Qui `id`
    resta la PK condivisa con contatti_pz e `cartella_clinica` è una colonna
    normale indicizzata.

    `parente_id` (→Parenti) è un FK-placeholder Integer: quella tabella non è
    ancora modellata (vedi Backlog).
    """

    __tablename__ = "prericoveri"

    id: Mapped[int] = mapped_column(ForeignKey("contatti_pz.id"), primary_key=True)

    regime_ricovero: Mapped[
        Literal["Ordinario", "DHDS", "DayService", "PreRicovero", "PreRicoveroDH"] | None
    ] = mapped_column(String(20), default=None)
    disciplina_ricovero_id: Mapped[int | None] = mapped_column(
        ForeignKey("discipline.id"), default=None
    )
    data_inizio: Mapped[date | None] = mapped_column(Date, default=None)
    data_fine: Mapped[date | None] = mapped_column(Date, default=None)
    cartella_clinica: Mapped[int | None] = mapped_column(Integer, default=None, index=True)
    modalita_accesso_id: Mapped[int | None] = mapped_column(
        ForeignKey("modalita_accesso.id"), default=None
    )
    scheda_e: Mapped[bool | None] = mapped_column(Boolean, default=None)

    codice_impegnativa: Mapped[str | None] = mapped_column(String(7), default=None)
    numero_impegnativa: Mapped[str | None] = mapped_column(String(11), default=None)
    data_impegnativa: Mapped[date | None] = mapped_column(Date, default=None)

    provenienza_id: Mapped[int | None] = mapped_column(ForeignKey("provenienze.id"), default=None)
    diagnosi_ingresso_id: Mapped[int | None] = mapped_column(
        ForeignKey("diagnosi.id"), default=None
    )
    medico_inviante_id: Mapped[int | None] = mapped_column(
        ForeignKey("medici_esterni.id"), default=None
    )
    prenotazione_id: Mapped[int | None] = mapped_column(ForeignKey("prenotazioni.id"), default=None)
    locked_user_id: Mapped[int | None] = mapped_column(ForeignKey("dipendenti.id"), default=None)

    specialista_medico_id: Mapped[int | None] = mapped_column(ForeignKey("medici.id"), default=None)
    specialista_chirurgo_id: Mapped[int | None] = mapped_column(
        ForeignKey("medici.id"), default=None
    )
    tutor_id: Mapped[int | None] = mapped_column(ForeignKey("medici.id"), default=None)
    # FK-placeholder verso Parenti (non ancora modellato - vedi Backlog)
    parente_id: Mapped[int | None] = mapped_column(Integer, default=None)

    note_amministrative: Mapped[str | None] = mapped_column(String(250), default=None)
    note_cliniche: Mapped[str | None] = mapped_column(String(250), default=None)
    computer: Mapped[str | None] = mapped_column(String(50), default=None)
    anno_prericovero: Mapped[int | None] = mapped_column(Integer, default=None)
    mese_prericovero: Mapped[
        Literal[
            "Gennaio",
            "Febbraio",
            "Marzo",
            "Aprile",
            "Maggio",
            "Giugno",
            "Luglio",
            "Agosto",
            "Settembre",
            "Ottobre",
            "Novembre",
            "Dicembre",
        ]
        | None
    ] = mapped_column(String(10), default=None)

    disciplina_ricovero: Mapped["Disciplina | None"] = relationship()
    modalita_accesso: Mapped["ModalitaAccesso | None"] = relationship()
    provenienza: Mapped["Provenienza | None"] = relationship()
    diagnosi_ingresso: Mapped["Diagnosi | None"] = relationship()
    medico_inviante: Mapped["MedicoEsterno | None"] = relationship()
    locked_user: Mapped["Dipendente | None"] = relationship(foreign_keys=[locked_user_id])
    specialista_medico: Mapped["Medico | None"] = relationship(foreign_keys=[specialista_medico_id])
    specialista_chirurgo: Mapped["Medico | None"] = relationship(
        foreign_keys=[specialista_chirurgo_id]
    )
    tutor: Mapped["Medico | None"] = relationship(foreign_keys=[tutor_id])
    prenotazione: Mapped["Prenotazione | None"] = relationship(
        back_populates="prericovero", foreign_keys=[prenotazione_id]
    )
    ricovero: Mapped["Ricovero | None"] = relationship(
        back_populates="prericovero",
        uselist=False,
        foreign_keys="Ricovero.prericovero_id",
    )

    __mapper_args__ = {
        "polymorphic_identity": "prericovero",
        "inherit_condition": id == ContattoPz.id,
    }
