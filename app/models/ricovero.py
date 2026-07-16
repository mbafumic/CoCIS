from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.contatto_pz import ContattoPz

if TYPE_CHECKING:
    from app.models.prenotazione import Prenotazione
    from app.models.prericovero import Prericovero


class Ricovero(ContattoPz):
    """Ricovero ospedaliero: sottotipo concreto di ContattoPz.

    id è sia PK che FK verso contatti_pz.id (PK condivisa, come nel legacy).
    Future slice aggiungeranno figli con FK stabile su ricoveri.id (SchedaClinica,
    Rilevazioni, ProcedurePreviste/Effettuate, SDO/SDO10).

    Un Ricovero può nascere direttamente da una Prenotazione (caso urgente) oppure
    passare da un Prericovero: entrambi i link sono opzionali e le FK reali stanno
    qui (nel legacy i reverse su Prenotazione erano proprietà calcolate).
    """

    __tablename__ = "ricoveri"

    id: Mapped[int] = mapped_column(ForeignKey("contatti_pz.id"), primary_key=True)
    reparto: Mapped[str] = mapped_column(String(100))
    data_ricovero: Mapped[date] = mapped_column(Date)
    data_dimissione: Mapped[date | None] = mapped_column(Date, default=None)
    stato: Mapped[str] = mapped_column(String(20), default="aperto")

    prenotazione_id: Mapped[int | None] = mapped_column(ForeignKey("prenotazioni.id"), default=None)
    prericovero_id: Mapped[int | None] = mapped_column(ForeignKey("prericoveri.id"), default=None)

    prenotazione: Mapped["Prenotazione | None"] = relationship(
        back_populates="ricovero", foreign_keys=[prenotazione_id]
    )
    prericovero: Mapped["Prericovero | None"] = relationship(
        back_populates="ricovero", foreign_keys=[prericovero_id]
    )

    __mapper_args__ = {
        "polymorphic_identity": "ricovero",
        "inherit_condition": id == ContattoPz.id,
    }
