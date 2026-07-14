from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Professione(Base):
    __tablename__ = "professioni"

    id: Mapped[int] = mapped_column(primary_key=True)
    professione: Mapped[str] = mapped_column(String(30))
