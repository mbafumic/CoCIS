from datetime import date, datetime
from typing import TYPE_CHECKING, Literal

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, LargeBinary, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.comune import Comune
    from app.models.presidio_osp import PresidioOsp
    from app.models.rapporto_dipendenza import RapportoDipendenza
    from app.models.tipo_dipendente import TipoDipendente
    from app.models.titolo import Titolo


class Dipendente(Base):
    """Personale della struttura.

    Nel legacy estende `PermissionPolicyUser` (base sicurezza DevExpress): quella
    infrastruttura (username/password/ruoli/audit XPO) non viene migrata, si
    reimplementa nativamente. Qui restano i soli campi di dominio.

    `reparto_predefinito_id` referenzia `Reparti`, tabella grande di dominio proprio
    (anagrafica organizzativa) non ancora modellata: è un FK-placeholder (Integer
    nullable) finché `reparti` non sarà modellata. La relazione uno-a-molti inversa
    con Reparti (un dipendente afferisce a più reparti) segue nella stessa slice.
    """

    __tablename__ = "dipendenti"

    id: Mapped[int] = mapped_column(primary_key=True)

    # Anagrafica
    cognome: Mapped[str] = mapped_column(String(30))
    nome: Mapped[str] = mapped_column(String(30))
    data_nascita: Mapped[date | None] = mapped_column(Date, default=None)
    sesso: Mapped[Literal["M", "F"] | None] = mapped_column(String(1), default=None)
    comune_nascita_id: Mapped[int | None] = mapped_column(ForeignKey("comuni.id"), default=None)
    codice_fiscale: Mapped[str | None] = mapped_column(String(16), default=None)
    partita_iva: Mapped[str | None] = mapped_column(String(11), default=None)
    comune_residenza_id: Mapped[int | None] = mapped_column(ForeignKey("comuni.id"), default=None)
    indirizzo: Mapped[str | None] = mapped_column(String(80), default=None)
    telefono: Mapped[str | None] = mapped_column(String(20), default=None)
    cellulare: Mapped[str | None] = mapped_column(String(20), default=None)

    # Rapporto di lavoro
    rapporto_dipendenza_id: Mapped[int | None] = mapped_column(
        ForeignKey("rapporti_dipendenza.id"), default=None
    )
    data_inizio_rapporto: Mapped[date | None] = mapped_column(Date, default=None)
    data_fine_rapporto: Mapped[date | None] = mapped_column(Date, default=None)
    badge: Mapped[str | None] = mapped_column(String(20), default=None)
    sigla: Mapped[str | None] = mapped_column(String(6), default=None)
    titolo_id: Mapped[int | None] = mapped_column(ForeignKey("titoli.id"), default=None)
    tipo_dipendente_id: Mapped[int | None] = mapped_column(
        ForeignKey("tipi_dipendente.id"), default=None
    )
    presidio_id: Mapped[int | None] = mapped_column(ForeignKey("presidi_osp.id"), default=None)
    reparto_predefinito_id: Mapped[int | None] = mapped_column(Integer, default=None)

    # Email / posta
    email: Mapped[str | None] = mapped_column(String(60), default=None)
    utente_email: Mapped[str | None] = mapped_column(String(60), default=None)
    password_email: Mapped[str | None] = mapped_column(String(30), default=None)
    pec: Mapped[str | None] = mapped_column(String(70), default=None)

    # Preferenze/flag applicativi (BooleanEnum nel legacy - tri-stato nullable)
    elenco_globale: Mapped[bool | None] = mapped_column(Boolean, default=None)
    documentix_sezione: Mapped[bool | None] = mapped_column(Boolean, default=None)
    mostra_ricoveri: Mapped[bool | None] = mapped_column(Boolean, default=None)
    mostra_sala_operatoria: Mapped[bool | None] = mapped_column(Boolean, default=None)
    richiesta_emocomponenti: Mapped[bool | None] = mapped_column(Boolean, default=None)
    segreteria: Mapped[bool] = mapped_column(Boolean, default=False)
    no_intestazione_referti_amb: Mapped[bool] = mapped_column(Boolean, default=False)
    presenza_omonimo: Mapped[bool] = mapped_column(Boolean, default=False)
    avvisato: Mapped[bool] = mapped_column(Boolean, default=False)

    # Firma / FSE (enum legacy memorizzati come nome del membro)
    firma_digitalizzata: Mapped[bytes | None] = mapped_column(LargeBinary, default=None)
    tipo_firma: Mapped[Literal["Standard", "DigitaleLocale", "DigitaleRemota"] | None] = (
        mapped_column(String(20), default=None)
    )
    stato_fse: Mapped[Literal["SoloFirma", "SoloInvio", "InvioEFirma"] | None] = mapped_column(
        String(20), default=None
    )
    password_changed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None
    )
    tipo_rilevazione_inventario: Mapped[Literal["Umi", "Cnf"] | None] = mapped_column(
        String(10), default=None
    )

    # Varie
    pin_web: Mapped[str | None] = mapped_column(String(10), default=None)
    nodo_startup: Mapped[str | None] = mapped_column(String(100), default=None)
    codice_esterno: Mapped[int | None] = mapped_column(Integer, default=None)
    id_esterno: Mapped[int | None] = mapped_column(Integer, default=None)
    avviso: Mapped[str | None] = mapped_column(Text, default=None)

    comune_nascita: Mapped["Comune | None"] = relationship(foreign_keys=[comune_nascita_id])
    comune_residenza: Mapped["Comune | None"] = relationship(foreign_keys=[comune_residenza_id])
    rapporto_dipendenza: Mapped["RapportoDipendenza | None"] = relationship()
    titolo: Mapped["Titolo | None"] = relationship()
    tipo_dipendente: Mapped["TipoDipendente | None"] = relationship()
    presidio: Mapped["PresidioOsp | None"] = relationship(back_populates="dipendenti")

    @property
    def nominativo(self) -> str:
        """Es. 'Rossi Mario'. Calcolato, non persistito (era un PersistentAlias)."""
        return f"{self.cognome} {self.nome}"
