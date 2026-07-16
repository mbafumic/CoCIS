from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.dipendente import Dipendente


class Disciplina(Base):
    """Disciplina/unità funzionale (codifica ministeriale del reparto di degenza).

    `reparto_degenza_id` referenzia `Reparti`, non ancora modellato (dominio
    anagrafica organizzativa — vedi Backlog): è un FK-placeholder Integer nullable.
    """

    __tablename__ = "discipline"

    id: Mapped[int] = mapped_column(primary_key=True)
    codice: Mapped[str | None] = mapped_column(String(2), default=None)
    disciplina: Mapped[str | None] = mapped_column(String(50), default=None)
    attiva: Mapped[bool | None] = mapped_column(Boolean, default=None)
    trasferimento_interno: Mapped[bool | None] = mapped_column(Boolean, default=None)
    standard_procedure: Mapped[str | None] = mapped_column(String(100), default=None)
    gg_terapia_fino_sosp: Mapped[int | None] = mapped_column(Integer, default=None)
    allegati_cc: Mapped[bool | None] = mapped_column(Boolean, default=None)
    responsabile_id: Mapped[int | None] = mapped_column(ForeignKey("dipendenti.id"), default=None)
    reparto_degenza_id: Mapped[int | None] = mapped_column(Integer, default=None)

    responsabile: Mapped["Dipendente | None"] = relationship()
