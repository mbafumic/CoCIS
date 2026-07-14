from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class PosizioneProfessionale(Base):
    __tablename__ = "posizioni_professionali"

    id: Mapped[int] = mapped_column(primary_key=True)
    posizione: Mapped[str] = mapped_column(String(30))
