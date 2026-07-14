from datetime import date, datetime
from typing import TYPE_CHECKING, Literal

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.comune import Comune
    from app.models.contatto_pz import ContattoPz
    from app.models.gruppo_sanguigno import GruppoSanguigno


class Paziente(Base):
    __tablename__ = "pazienti"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    cognome: Mapped[str] = mapped_column(String(100))
    data_nascita: Mapped[date] = mapped_column(Date)
    codice_fiscale: Mapped[str] = mapped_column(String(16), unique=True, index=True)
    sesso: Mapped[Literal["M", "F"] | None] = mapped_column(String(1), default=None)
    # stringa libera nel legacy (es. "45"), non ricalcolata automaticamente da data_nascita
    eta: Mapped[str | None] = mapped_column(String(9), default=None)

    luogo_nascita_id: Mapped[int | None] = mapped_column(ForeignKey("comuni.id"), default=None)
    gruppo_sanguigno_id: Mapped[int | None] = mapped_column(
        ForeignKey("gruppi_sanguigni.id"), default=None
    )

    # tri-stato nel legacy (BooleanEnum: No/Si, colonna nullable) - None = non rilevato
    deceduto: Mapped[bool | None] = mapped_column(Boolean, default=None)
    testimone_di_geova: Mapped[bool | None] = mapped_column(Boolean, default=None)

    telefoni_paziente: Mapped[str | None] = mapped_column(String(200), default=None)
    telefoni_parenti: Mapped[str | None] = mapped_column(String(200), default=None)

    # consensi privacy (trattamento dati personali, dossier sanitario)
    consenso_tratt_pers: Mapped[bool] = mapped_column(Boolean, default=False)
    consenso_dossier: Mapped[bool] = mapped_column(Boolean, default=False)

    download_referti: Mapped[str | None] = mapped_column(String(20), default=None)
    codice_esterno: Mapped[int | None] = mapped_column(Integer, default=None)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    luogo_nascita: Mapped["Comune | None"] = relationship()
    gruppo_sanguigno: Mapped["GruppoSanguigno | None"] = relationship()
    contatti: Mapped[list["ContattoPz"]] = relationship(back_populates="paziente")

    @property
    def nominativo(self) -> str:
        """Es. 'Rossi Mario'. Calcolato, non persistito (era un PersistentAlias)."""
        return f"{self.cognome.strip()} {self.nome.strip()}"

    @property
    def iniziali(self) -> str:
        """Es. 'R.M.'. Calcolato, non persistito."""
        iniziali = "".join(f"{parola[0]}." for parola in self.cognome.split() if parola)
        iniziali += " "
        iniziali += "".join(f"{parola[0]}." for parola in self.nome.split() if parola)
        return iniziali
