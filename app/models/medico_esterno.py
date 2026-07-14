from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.asp import Asp
    from app.models.comune import Comune


class MedicoEsterno(Base):
    """Medico curante esterno alla struttura (es. medico di base del paziente)."""

    __tablename__ = "medici_esterni"

    id: Mapped[int] = mapped_column(primary_key=True)
    cognome: Mapped[str | None] = mapped_column(String(30), default=None)
    nome: Mapped[str | None] = mapped_column(String(30), default=None)
    indirizzo: Mapped[str | None] = mapped_column(String(80), default=None)
    telefono: Mapped[str | None] = mapped_column(String(30), default=None)
    cellulare: Mapped[str | None] = mapped_column(String(20), default=None)
    citta_id: Mapped[int | None] = mapped_column(ForeignKey("comuni.id"), default=None)
    codice_regionale: Mapped[str | None] = mapped_column(String(16), default=None)
    n_empam: Mapped[str | None] = mapped_column(String(10), default=None)
    asp_id: Mapped[int | None] = mapped_column(ForeignKey("asp.id"), default=None)
    specializzazione: Mapped[str | None] = mapped_column(String(50), default=None)
    codice_fiscale: Mapped[str | None] = mapped_column(String(16), default=None)

    citta: Mapped["Comune | None"] = relationship()
    asp: Mapped["Asp | None"] = relationship()

    @property
    def nominativo(self) -> str:
        """Calcolato, non persistito (era un PersistentAlias)."""
        if not self.nome:
            return self.cognome or ""
        return f"{self.cognome} {self.nome}"
