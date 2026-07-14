from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Stato(Base):
    """Stato estero/nazionalità (usato per cittadinanza e stato di residenza)."""

    __tablename__ = "stati"

    id: Mapped[int] = mapped_column(primary_key=True)
    stato: Mapped[str] = mapped_column(String(30))
    codice_istat: Mapped[str | None] = mapped_column(String(3), default=None)
    nazionalita: Mapped[str | None] = mapped_column(String(20), default=None)
    codice_iso: Mapped[str | None] = mapped_column(String(3), default=None)
    # tri-stato nel legacy (BooleanEnum) - None = non rilevato
    comunitario: Mapped[bool | None] = mapped_column(Boolean, default=None)

    @property
    def istat_stato(self) -> str:
        """Es. '203 - Francia'. Calcolato, non persistito (era un PersistentAlias)."""
        return f"{self.codice_istat} - {self.stato}"
