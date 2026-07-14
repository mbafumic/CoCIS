from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.comune import Comune
    from app.models.regione import Regione


class Asp(Base):
    """Azienda Sanitaria Provinciale di riferimento."""

    __tablename__ = "asp"

    id: Mapped[int] = mapped_column(primary_key=True)
    azienda: Mapped[str | None] = mapped_column(String(3), default=None)
    denominazione: Mapped[str | None] = mapped_column(String(50), default=None)
    indirizzo: Mapped[str | None] = mapped_column(String(50), default=None)
    cap: Mapped[str | None] = mapped_column(String(6), default=None)
    citta_id: Mapped[int | None] = mapped_column(ForeignKey("comuni.id"), default=None)
    regione_id: Mapped[int | None] = mapped_column(ForeignKey("regioni.id"), default=None)
    anno: Mapped[int | None] = mapped_column(Integer, default=None)
    partita_iva: Mapped[str | None] = mapped_column(String(11), default=None)

    citta: Mapped["Comune | None"] = relationship()
    regione: Mapped["Regione | None"] = relationship()

    @property
    def codice_denominazione(self) -> str:
        """Es. 'MI3 - ASP Milano - Lombardia'. Calcolato, non persistito."""
        base = f"{self.azienda} - {self.denominazione}"
        if self.regione is not None:
            base += f" - {self.regione.regione}"
        return base
