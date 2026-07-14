from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class CategoriaPaziente(Base):
    __tablename__ = "categorie_paziente"

    id: Mapped[int] = mapped_column(primary_key=True)
    categoria: Mapped[str] = mapped_column(String(50))
