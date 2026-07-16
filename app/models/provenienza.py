from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Provenienza(Base):
    """Provenienza del paziente all'accesso (con validità temporale della voce)."""

    __tablename__ = "provenienze"

    id: Mapped[int] = mapped_column(primary_key=True)
    provenienza: Mapped[str] = mapped_column(String(70))
    anno_inizio_validita: Mapped[int | None] = mapped_column(Integer, default=None)
    anno_fine_validita: Mapped[int | None] = mapped_column(Integer, default=None)
