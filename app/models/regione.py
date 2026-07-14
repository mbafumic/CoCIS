from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Regione(Base):
    __tablename__ = "regioni"

    id: Mapped[int] = mapped_column(primary_key=True)
    regione: Mapped[str] = mapped_column(String(25))
    codice: Mapped[str | None] = mapped_column(String(3), default=None)
    ordine_stampa: Mapped[int | None] = mapped_column(Integer, default=None)
