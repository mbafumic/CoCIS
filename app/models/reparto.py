from datetime import date, datetime
from typing import TYPE_CHECKING, Literal

from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.dipendente import Dipendente
    from app.models.presidio_osp import PresidioOsp

# M:M reparti <-> dipendenti (association "Reparti-Dipendenti" nel legacy).
# Nota: nel dump SQL esiste anche `repartireparti_medicimedici`, ma nessun oggetto
# XPO la dichiara: e' un residuo legacy non mappato e non viene modellata.
reparti_dipendenti = Table(
    "reparti_dipendenti",
    Base.metadata,
    Column("reparto_id", ForeignKey("reparti.id"), primary_key=True),
    Column("dipendente_id", ForeignKey("dipendenti.id"), primary_key=True),
)


class Reparto(Base):
    """Reparto/unità operativa di un presidio ospedaliero.

    `reparto_mag_id` e `reparto_trasf_mag_id` sono self-riferimenti: indicano il
    reparto di riferimento per il magazzino e per i trasferimenti di magazzino.
    """

    __tablename__ = "reparti"

    id: Mapped[int] = mapped_column(primary_key=True)
    reparto: Mapped[str | None] = mapped_column(String(50), default=None)
    sigla: Mapped[str | None] = mapped_column(String(11), default=None)
    tipo: Mapped[Literal["Degenza", "Servizio", "Supporto"] | None] = mapped_column(
        String(20), default=None
    )
    presidio_id: Mapped[int | None] = mapped_column(ForeignKey("presidi_osp.id"), default=None)

    letti_accreditati: Mapped[int | None] = mapped_column(Integer, default=None)
    letti_non_accreditati: Mapped[int | None] = mapped_column(Integer, default=None)
    no_check_letto_occupato: Mapped[bool] = mapped_column(Boolean, default=False)

    # magazzino
    tipo_magazzino: Mapped[Literal["Centrale", "Reparto", "Nessuno"] | None] = mapped_column(
        String(20), default=None
    )
    reparto_mag_id: Mapped[int | None] = mapped_column(ForeignKey("reparti.id"), default=None)
    reparto_trasf_mag_id: Mapped[int | None] = mapped_column(ForeignKey("reparti.id"), default=None)

    # flag operativi (BooleanEnum nel legacy - tri-stato nullable)
    accetta_trasferimenti: Mapped[bool | None] = mapped_column(Boolean, default=None)
    effettua_procedure: Mapped[bool | None] = mapped_column(Boolean, default=None)
    gestione_notizie_cliniche: Mapped[bool | None] = mapped_column(Boolean, default=None)

    # terapia / somministrazioni
    gestione_terapia: Mapped[bool] = mapped_column(Boolean, default=False)
    data_avvio_terapia: Mapped[date | None] = mapped_column(Date, default=None)
    ora_validazione_terapia: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None
    )
    max_anticipo_somministrazione: Mapped[int | None] = mapped_column(Integer, default=None)
    max_posticipo_somministrazione: Mapped[int | None] = mapped_column(Integer, default=None)
    ora_insulina_colazione: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None
    )
    ora_insulina_pranzo: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None
    )
    ora_insulina_cena: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None
    )
    ora_insulina_sera: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None
    )

    codice_lis: Mapped[str | None] = mapped_column(String(10), default=None)
    diario_fkt: Mapped[bool] = mapped_column(Boolean, default=False)
    consegne_lavagna: Mapped[bool] = mapped_column(Boolean, default=False)
    print_order: Mapped[int | None] = mapped_column(Integer, default=None)
    standard_procedure_giorno: Mapped[str | None] = mapped_column(String(100), default=None)
    standard_procedure_cipi_giorno: Mapped[str | None] = mapped_column(String(150), default=None)
    personale_docwin: Mapped[str | None] = mapped_column(String(40), default=None)
    shutdown_time: Mapped[int | None] = mapped_column(Integer, default=None)

    presidio: Mapped["PresidioOsp | None"] = relationship(back_populates="reparti")
    reparto_mag: Mapped["Reparto | None"] = relationship(
        remote_side=[id], foreign_keys=[reparto_mag_id]
    )
    reparto_trasf_mag: Mapped["Reparto | None"] = relationship(
        remote_side=[id], foreign_keys=[reparto_trasf_mag_id]
    )
    dipendenti: Mapped[list["Dipendente"]] = relationship(
        secondary=reparti_dipendenti, back_populates="reparti"
    )
