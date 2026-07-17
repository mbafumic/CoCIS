from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, LargeBinary, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.asp import Asp
    from app.models.comune import Comune
    from app.models.dipendente import Dipendente
    from app.models.medico import Medico
    from app.models.reparto import Reparto


class PresidioOsp(Base):
    """Presidio ospedaliero (sede fisica della struttura).

    `direttore_sanitario_id` e `responsabile_dipartimento_id` referenziano `Medico`
    ma **non hanno una FK a DB**, di proposito: creerebbero un ciclo
    `presidi_osp → medici → dipendenti → presidi_osp`. Il legacy risolve allo stesso
    modo (`[NoForeignKey]`: nel dump SQL l'unico constraint di `presidiosp` è
    `Comune`). Le relationship qui sotto le rendono comunque navigabili dall'ORM.
    """

    __tablename__ = "presidi_osp"

    id: Mapped[int] = mapped_column(primary_key=True)
    presidio: Mapped[str | None] = mapped_column(String(100), default=None)
    comune_id: Mapped[int | None] = mapped_column(ForeignKey("comuni.id"), default=None)
    indirizzo: Mapped[str | None] = mapped_column(String(60), default=None)
    cap: Mapped[str | None] = mapped_column(String(6), default=None)
    tel: Mapped[str | None] = mapped_column(String(20), default=None)
    fax: Mapped[str | None] = mapped_column(String(20), default=None)
    email: Mapped[str | None] = mapped_column(String(50), default=None)
    asp_id: Mapped[int | None] = mapped_column(ForeignKey("asp.id"), default=None)

    # Intestazioni/piè di pagina RTF per stampe (documenti clinici, fatture)
    header: Mapped[str | None] = mapped_column(Text, default=None)
    footer: Mapped[str | None] = mapped_column(Text, default=None)
    header_fattura: Mapped[str | None] = mapped_column(Text, default=None)
    header_clinico: Mapped[str | None] = mapped_column(Text, default=None)

    # Configurazione invio email
    smtp: Mapped[str | None] = mapped_column(String(50), default=None)
    mail_host: Mapped[str | None] = mapped_column(String(50), default=None)
    smtp_port: Mapped[int | None] = mapped_column(Integer, default=None)

    home_page: Mapped[bytes | None] = mapped_column(LargeBinary, default=None)

    # Riferimenti a Medico senza FK a DB (ciclo) - vedi docstring
    direttore_sanitario_id: Mapped[int | None] = mapped_column(Integer, default=None)
    responsabile_dipartimento_id: Mapped[int | None] = mapped_column(Integer, default=None)

    comune: Mapped["Comune | None"] = relationship()
    asp: Mapped["Asp | None"] = relationship()
    dipendenti: Mapped[list["Dipendente"]] = relationship(
        back_populates="presidio", foreign_keys="Dipendente.presidio_id"
    )
    reparti: Mapped[list["Reparto"]] = relationship(back_populates="presidio")
    direttore_sanitario: Mapped["Medico | None"] = relationship(
        primaryjoin="foreign(PresidioOsp.direttore_sanitario_id) == Medico.id",
        viewonly=True,
    )
    responsabile_dipartimento: Mapped["Medico | None"] = relationship(
        primaryjoin="foreign(PresidioOsp.responsabile_dipartimento_id) == Medico.id",
        viewonly=True,
    )
