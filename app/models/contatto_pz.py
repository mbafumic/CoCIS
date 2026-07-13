from datetime import date, datetime
from typing import TYPE_CHECKING

from sqlalchemy import Date, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.paziente import Paziente


class ContattoPz(Base):
    """Base polimorfica per ogni contatto/interazione paziente-struttura.

    Nel legacy (DevExpress XPO) i sottotipi condividono l'OID come PK+FK verso
    ContattoPz (class-table inheritance). Qui replichiamo lo stesso pattern con
    joined-table inheritance nativa SQLAlchemy: ogni sottotipo concreto (Ricovero,
    e in slice future Prericovero/PrenotazioneAmbulatorio/PrestazioneAmbulatoriale)
    è una tabella propria con PK condivisa.
    """

    __tablename__ = "contatti_pz"

    id: Mapped[int] = mapped_column(primary_key=True)
    paziente_id: Mapped[int] = mapped_column(ForeignKey("pazienti.id"), index=True)
    tipo_contatto: Mapped[str] = mapped_column(String(50))
    data_apertura: Mapped[date] = mapped_column(Date)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    paziente: Mapped["Paziente"] = relationship(back_populates="contatti")

    __mapper_args__ = {
        "polymorphic_on": "tipo_contatto",
        "polymorphic_identity": "contatto_pz",
    }
