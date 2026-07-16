from datetime import date, datetime
from typing import TYPE_CHECKING, Literal

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.contatto_pz import ContattoPz

if TYPE_CHECKING:
    from app.models.diagnosi import Diagnosi
    from app.models.disciplina import Disciplina
    from app.models.disdetta_prenotazione import DisdettaPrenotazione
    from app.models.grado_urgenza import GradoUrgenza
    from app.models.medico_esterno import MedicoEsterno
    from app.models.modalita_accesso import ModalitaAccesso
    from app.models.prericovero import Prericovero
    from app.models.ricovero import Ricovero


class Prenotazione(ContattoPz):
    """Prenotazione di ricovero: sottotipo concreto di ContattoPz.

    `regime_ricovero` distingue i casi che nel legacy erano 5 classi separate
    (PrenotazioniOrd/DH/DayService/PreRic/PreRicDH): erano mappate sulla tabella
    padre (`MapInheritance.ParentTable`), senza tabella propria, quindi qui sono
    semplicemente un valore di questo campo.

    `ricovero` e `prericovero` sono relationship inverse: nel legacy erano
    proprietà `[NonPersistent]` calcolate con una query, non colonne. Le FK reali
    stanno sui figli (Ricovero.prenotazione_id, Prericovero.prenotazione_id).

    `specialista_medico_id`/`specialista_chirurgo_id`/`tutor_id` referenziano
    `Medici`, non ancora modellato: sono FK-placeholder Integer (vedi Backlog).
    """

    __tablename__ = "prenotazioni"

    id: Mapped[int] = mapped_column(ForeignKey("contatti_pz.id"), primary_key=True)

    data: Mapped[date | None] = mapped_column(Date, default=None)
    regime_ricovero: Mapped[
        Literal["Ordinario", "DHDS", "DayService", "PreRicovero", "PreRicoveroDH"] | None
    ] = mapped_column(String(20), default=None)
    data_prevista_ricovero: Mapped[date | None] = mapped_column(Date, default=None)
    ora_ricovero: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    data_prev_pre_ric: Mapped[date | None] = mapped_column(Date, default=None)
    data_tampone: Mapped[date | None] = mapped_column(Date, default=None)

    grado_urgenza_id: Mapped[int | None] = mapped_column(
        ForeignKey("gradi_urgenza.id"), default=None
    )
    unita_funzionale_id: Mapped[int | None] = mapped_column(
        ForeignKey("discipline.id"), default=None
    )
    diagnosi_ingresso_id: Mapped[int | None] = mapped_column(
        ForeignKey("diagnosi.id"), default=None
    )
    modalita_accesso_id: Mapped[int | None] = mapped_column(
        ForeignKey("modalita_accesso.id"), default=None
    )
    medico_inviante_id: Mapped[int | None] = mapped_column(
        ForeignKey("medici_esterni.id"), default=None
    )

    # FK-placeholder verso Medici (non ancora modellato)
    specialista_medico_id: Mapped[int | None] = mapped_column(Integer, default=None)
    specialista_chirurgo_id: Mapped[int | None] = mapped_column(Integer, default=None)
    tutor_id: Mapped[int | None] = mapped_column(Integer, default=None)

    note_amministrative: Mapped[str | None] = mapped_column(String(250), default=None)
    note_cliniche: Mapped[str | None] = mapped_column(String(255), default=None)

    classe_priorita: Mapped[Literal["A", "B", "C", "D"] | None] = mapped_column(
        String(1), default=None
    )
    motivo_dh: Mapped[
        Literal["Diagnostico", "Chirurgico", "Terapeutico", "Riabilitativo"] | None
    ] = mapped_column(String(20), default=None)
    stato: Mapped[Literal["DaEvadere", "Evasa", "Bloccata", "Disdetta", "EvasoPreric"] | None] = (
        mapped_column(String(20), default=None)
    )

    bloccato: Mapped[bool | None] = mapped_column(Boolean, default=None)
    data_blocco: Mapped[date | None] = mapped_column(Date, default=None)

    email: Mapped[str | None] = mapped_column(String(60), default=None)
    camera_singola: Mapped[bool] = mapped_column(Boolean, default=False)
    data_avviso: Mapped[date | None] = mapped_column(Date, default=None)
    avvisato: Mapped[bool] = mapped_column(Boolean, default=False)

    grado_urgenza: Mapped["GradoUrgenza | None"] = relationship()
    unita_funzionale: Mapped["Disciplina | None"] = relationship()
    diagnosi_ingresso: Mapped["Diagnosi | None"] = relationship()
    modalita_accesso: Mapped["ModalitaAccesso | None"] = relationship()
    medico_inviante: Mapped["MedicoEsterno | None"] = relationship()
    # foreign_keys esplicite: i sottotipi condividono la PK con contatti_pz, quindi
    # senza indicazione SQLAlchemy trova più percorsi FK possibili.
    disdetta: Mapped["DisdettaPrenotazione | None"] = relationship(
        back_populates="prenotazione",
        uselist=False,
        foreign_keys="DisdettaPrenotazione.prenotazione_id",
    )
    prericovero: Mapped["Prericovero | None"] = relationship(
        back_populates="prenotazione",
        uselist=False,
        foreign_keys="Prericovero.prenotazione_id",
    )
    ricovero: Mapped["Ricovero | None"] = relationship(
        back_populates="prenotazione",
        uselist=False,
        foreign_keys="Ricovero.prenotazione_id",
    )

    __mapper_args__ = {
        "polymorphic_identity": "prenotazione",
        "inherit_condition": id == ContattoPz.id,
    }
