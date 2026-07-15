from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class RapportoDipendenza(Base):
    """Tipo di rapporto di dipendenza (es. Tempo indeterminato, Convenzione...)."""

    __tablename__ = "rapporti_dipendenza"

    id: Mapped[int] = mapped_column(primary_key=True)
    rapporto: Mapped[str] = mapped_column(String(40))
