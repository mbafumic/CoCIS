from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.comune import Comune


class PresidioOsp(Base):
    """Presidio ospedaliero (sede fisica della struttura). Versione minima: solo
    identificazione e indirizzo - i campi di configurazione stampa/email del
    legacy (header/footer documenti, SMTP) non sono dati di dominio e non vanno
    portati. L'anagrafica organizzativa completa (GlobalModule) è una slice futura.
    """

    __tablename__ = "presidi_osp"

    id: Mapped[int] = mapped_column(primary_key=True)
    presidio: Mapped[str | None] = mapped_column(String(100), default=None)
    comune_id: Mapped[int | None] = mapped_column(ForeignKey("comuni.id"), default=None)
    indirizzo: Mapped[str | None] = mapped_column(String(100), default=None)
    cap: Mapped[str | None] = mapped_column(String(6), default=None)
    prov: Mapped[str | None] = mapped_column(String(2), default=None)
    tel: Mapped[str | None] = mapped_column(String(30), default=None)
    fax: Mapped[str | None] = mapped_column(String(30), default=None)
    email: Mapped[str | None] = mapped_column(String(80), default=None)

    comune: Mapped["Comune | None"] = relationship()
