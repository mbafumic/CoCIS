from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, LargeBinary, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.asp import Asp
    from app.models.comune import Comune
    from app.models.dipendente import Dipendente


class PresidioOsp(Base):
    """Presidio ospedaliero (sede fisica della struttura).

    `direttore_sanitario_id` e `responsabile_dipartimento_id` referenziano
    `Medici` nel legacy: `Medici` non è ancora modellato (è un sottotipo di
    `Dipendente`, dominio staff medico — vedi Backlog), quindi qui sono FK-placeholder
    (Integer nullable, diventeranno FK vere quando la tabella medici sarà modellata).
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

    # FK-placeholder verso Medici (non ancora modellato) - vedi docstring
    direttore_sanitario_id: Mapped[int | None] = mapped_column(Integer, default=None)
    responsabile_dipartimento_id: Mapped[int | None] = mapped_column(Integer, default=None)

    comune: Mapped["Comune | None"] = relationship()
    asp: Mapped["Asp | None"] = relationship()
    dipendenti: Mapped[list["Dipendente"]] = relationship(back_populates="presidio")
