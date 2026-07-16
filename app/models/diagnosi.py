from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Diagnosi(Base):
    """Diagnosi di uso corrente (scorciatoia interna verso un codice ICD9-CM).

    `icd9_cm_id` referenzia `ICD9_CM` del modulo codifiche cliniche, non ancora
    modellato (vedi Backlog): è un FK-placeholder Integer nullable.
    """

    __tablename__ = "diagnosi"

    id: Mapped[int] = mapped_column(primary_key=True)
    descrizione: Mapped[str | None] = mapped_column(String(60), default=None)
    abbreviazione: Mapped[str | None] = mapped_column(String(15), default=None)
    icd9_cm_id: Mapped[int | None] = mapped_column(Integer, default=None)
