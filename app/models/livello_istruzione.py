from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class LivelloIstruzione(Base):
    __tablename__ = "livelli_istruzione"

    id: Mapped[int] = mapped_column(primary_key=True)
    livello_istruzione: Mapped[str] = mapped_column(String(40))
