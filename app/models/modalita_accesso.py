from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class ModalitaAccesso(Base):
    """Modalità di accesso alla struttura (es. programmato, urgente)."""

    __tablename__ = "modalita_accesso"

    id: Mapped[int] = mapped_column(primary_key=True)
    modalita: Mapped[str] = mapped_column(String(50))
