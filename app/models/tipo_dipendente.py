from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class TipoDipendente(Base):
    """Tipo di dipendente (es. Medico, Infermiere, Tecnico...)."""

    __tablename__ = "tipi_dipendente"

    id: Mapped[int] = mapped_column(primary_key=True)
    tipo: Mapped[str] = mapped_column(String(30))
