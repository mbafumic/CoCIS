from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class StatoCivile(Base):
    __tablename__ = "stati_civili"

    id: Mapped[int] = mapped_column(primary_key=True)
    stato_civile: Mapped[str] = mapped_column(String(20))
