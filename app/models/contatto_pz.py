from datetime import date, datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Date, DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

if TYPE_CHECKING:
    from app.models.asp import Asp
    from app.models.categoria_paziente import CategoriaPaziente
    from app.models.comune import Comune
    from app.models.dipendente import Dipendente
    from app.models.livello_istruzione import LivelloIstruzione
    from app.models.medico_esterno import MedicoEsterno
    from app.models.paziente import Paziente
    from app.models.posizione_professionale import PosizioneProfessionale
    from app.models.presidio_osp import PresidioOsp
    from app.models.professione import Professione
    from app.models.stato import Stato
    from app.models.stato_civile import StatoCivile
    from app.models.tipo_documento import TipoDocumento


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

    # Anagrafica/domicilio al momento del contatto
    indirizzo: Mapped[str | None] = mapped_column(String(50), default=None)
    cap: Mapped[str | None] = mapped_column(String(6), default=None)
    comune_residenza_id: Mapped[int | None] = mapped_column(ForeignKey("comuni.id"), default=None)
    stato_residenza_id: Mapped[int | None] = mapped_column(ForeignKey("stati.id"), default=None)
    cittadinanza_id: Mapped[int | None] = mapped_column(ForeignKey("stati.id"), default=None)
    stato_civile_id: Mapped[int | None] = mapped_column(ForeignKey("stati_civili.id"), default=None)
    professione_id: Mapped[int | None] = mapped_column(ForeignKey("professioni.id"), default=None)
    posizione_professionale_id: Mapped[int | None] = mapped_column(
        ForeignKey("posizioni_professionali.id"), default=None
    )
    livello_istruzione_id: Mapped[int | None] = mapped_column(
        ForeignKey("livelli_istruzione.id"), default=None
    )
    categoria_paziente_id: Mapped[int | None] = mapped_column(
        ForeignKey("categorie_paziente.id"), default=None
    )

    # Documento di identità
    tipo_documento_id: Mapped[int | None] = mapped_column(
        ForeignKey("tipi_documento.id"), default=None
    )
    documento: Mapped[str | None] = mapped_column(String(20), default=None)
    data_rilascio: Mapped[date | None] = mapped_column(Date, default=None)
    ente_rilascio: Mapped[str | None] = mapped_column(String(40), default=None)

    # Riferimenti struttura/operatore
    medico_curante_id: Mapped[int | None] = mapped_column(
        ForeignKey("medici_esterni.id"), default=None
    )
    asp_residenza_id: Mapped[int | None] = mapped_column(ForeignKey("asp.id"), default=None)
    presidio_id: Mapped[int | None] = mapped_column(ForeignKey("presidi_osp.id"), default=None)
    operatore_id: Mapped[int | None] = mapped_column(ForeignKey("dipendenti.id"), default=None)

    # Dati clinici di base
    tessera_team: Mapped[str | None] = mapped_column(String(30), default=None)
    peso: Mapped[float | None] = mapped_column(Float, default=None)
    altezza: Mapped[int | None] = mapped_column(Integer, default=None)

    # TEAM/ENI-STP (assistenza sanitaria stranieri temporaneamente presenti)
    num_ist_team: Mapped[str | None] = mapped_column(String(50), default=None)
    ente_rilascio_eni_stp: Mapped[str | None] = mapped_column(String(50), default=None)
    data_rilascio_eni_stp: Mapped[date | None] = mapped_column(Date, default=None)
    data_scadenza_team_eni_stp: Mapped[date | None] = mapped_column(Date, default=None)

    # Privacy / consensi e dichiarazioni
    diniego_fse: Mapped[bool] = mapped_column(Boolean, default=False)
    nega_presenza_allergie: Mapped[bool] = mapped_column(Boolean, default=False)
    nega_presenza_patologie: Mapped[bool] = mapped_column(Boolean, default=False)
    nega_presenza_patologie_infettive: Mapped[bool] = mapped_column(Boolean, default=False)

    # Audit legacy (ultima modifica)
    last_update: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    pc_last_update: Mapped[str | None] = mapped_column(String(40), default=None)

    paziente: Mapped["Paziente"] = relationship(back_populates="contatti")
    comune_residenza: Mapped["Comune | None"] = relationship(foreign_keys=[comune_residenza_id])
    stato_residenza: Mapped["Stato | None"] = relationship(foreign_keys=[stato_residenza_id])
    cittadinanza: Mapped["Stato | None"] = relationship(foreign_keys=[cittadinanza_id])
    stato_civile: Mapped["StatoCivile | None"] = relationship()
    professione: Mapped["Professione | None"] = relationship()
    posizione_professionale: Mapped["PosizioneProfessionale | None"] = relationship()
    livello_istruzione: Mapped["LivelloIstruzione | None"] = relationship()
    categoria_paziente: Mapped["CategoriaPaziente | None"] = relationship()
    tipo_documento: Mapped["TipoDocumento | None"] = relationship()
    medico_curante: Mapped["MedicoEsterno | None"] = relationship()
    asp_residenza: Mapped["Asp | None"] = relationship()
    presidio: Mapped["PresidioOsp | None"] = relationship()
    operatore: Mapped["Dipendente | None"] = relationship()

    __mapper_args__ = {
        "polymorphic_on": "tipo_contatto",
        "polymorphic_identity": "contatto_pz",
    }

    @property
    def imc(self) -> float | None:
        """Indice di massa corporea (Kg/m^2). Calcolato, non persistito."""
        if not self.peso or not self.altezza:
            return None
        return round(self.peso / (self.altezza / 100) ** 2, 3)

    @property
    def superficie_corporea(self) -> float | None:
        """Superficie corporea (m^2), formula di Du Bois. Calcolata, non persistita."""
        if not self.peso or not self.altezza:
            return None
        return round((self.peso**0.425) * (self.altezza**0.725) * 0.007184, 3)
