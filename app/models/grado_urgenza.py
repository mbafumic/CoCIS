from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class GradoUrgenza(Base):
    """Grado di urgenza di una prenotazione di ricovero."""

    __tablename__ = "gradi_urgenza"

    id: Mapped[int] = mapped_column(primary_key=True)
    grado_urgenza: Mapped[str] = mapped_column(String(30))
    colore: Mapped[int | None] = mapped_column(Integer, default=None)
