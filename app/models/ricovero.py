from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.contatto_pz import ContattoPz


class Ricovero(ContattoPz):
    """Ricovero ospedaliero: sottotipo concreto di ContattoPz.

    id è sia PK che FK verso contatti_pz.id (PK condivisa, come nel legacy).
    Future slice aggiungeranno figli con FK stabile su ricoveri.id (SchedaClinica,
    Rilevazioni, ProcedurePreviste/Effettuate, SDO/SDO10) e link opzionali verso
    Prenotazione/Prericovero — nessuna di queste richiede modifiche a questa classe.
    """

    __tablename__ = "ricoveri"

    id: Mapped[int] = mapped_column(ForeignKey("contatti_pz.id"), primary_key=True)
    reparto: Mapped[str] = mapped_column(String(100))
    data_ricovero: Mapped[date] = mapped_column(Date)
    data_dimissione: Mapped[date | None] = mapped_column(Date, default=None)
    stato: Mapped[str] = mapped_column(String(20), default="aperto")

    __mapper_args__ = {
        "polymorphic_identity": "ricovero",
    }
