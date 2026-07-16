from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.prenotazione import Prenotazione


class DisdettaPrenotazione(Base):
    """Disdetta di una prenotazione (1:1 con Prenotazione).

    Nel legacy la 1:1 è circolare (`prenotazioni.DisdettaPrenotazione` **e**
    `disdettaprenotazione.Prenotazione`, entrambe colonne). Qui teniamo una sola
    FK, con la relationship inversa `Prenotazione.disdetta`: stessa informazione,
    nessun ciclo di FK.
    """

    __tablename__ = "disdetta_prenotazione"

    id: Mapped[int] = mapped_column(primary_key=True)
    motivo: Mapped[str | None] = mapped_column(String(200), default=None)
    prenotazione_id: Mapped[int | None] = mapped_column(
        ForeignKey("prenotazioni.id"), default=None, unique=True
    )

    prenotazione: Mapped["Prenotazione | None"] = relationship(back_populates="disdetta")
