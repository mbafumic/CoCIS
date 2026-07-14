from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.regione import Regione


class Comune(Base):
    __tablename__ = "comuni"

    id: Mapped[int] = mapped_column(primary_key=True)
    comune: Mapped[str] = mapped_column(String(35))
    istat: Mapped[str | None] = mapped_column(String(6), default=None)
    provincia: Mapped[str | None] = mapped_column(String(2), default=None)
    regione_id: Mapped[int | None] = mapped_column(ForeignKey("regioni.id"), default=None)
    prefisso: Mapped[str | None] = mapped_column(String(5), default=None)
    cap: Mapped[str | None] = mapped_column(String(5), default=None)
    cod_fisco: Mapped[str | None] = mapped_column(String(4), default=None)
    abitanti: Mapped[int | None] = mapped_column(Integer, default=None)

    regione: Mapped["Regione | None"] = relationship()

    @property
    def comune_provincia(self) -> str:
        """Es. 'Milano - MI - Lombardia'. Calcolato, non persistito (era un
        PersistentAlias nel legacy)."""
        base = f"{self.comune} - {self.provincia}"
        if self.regione is not None:
            base += f" - {self.regione.regione}"
        return base

    @property
    def comune_istat(self) -> str:
        """Es. 'Milano - 015146'. Calcolato, non persistito."""
        return f"{self.comune} - {self.istat}"
