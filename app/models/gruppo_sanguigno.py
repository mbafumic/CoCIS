from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class GruppoSanguigno(Base):
    __tablename__ = "gruppi_sanguigni"

    id: Mapped[int] = mapped_column(primary_key=True)
    gruppo: Mapped[str] = mapped_column(String(10))
    transcodifica: Mapped[str | None] = mapped_column(String(100), default=None)
