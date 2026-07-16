from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Titolo(Base):
    """Titolo del dipendente (es. Dott., Prof.)."""

    __tablename__ = "titoli"

    id: Mapped[int] = mapped_column(primary_key=True)
    titolo: Mapped[str] = mapped_column(String(10))
