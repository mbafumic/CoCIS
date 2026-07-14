from datetime import date

from pydantic import BaseModel, computed_field


class ContattoPzBase(BaseModel):
    """Campi condivisi da tutti i sottotipi di ContattoPz (Ricovero e, in slice
    future, Prericovero/PrenotazioneAmbulatorio/PrestazioneAmbulatoriale)."""

    indirizzo: str | None = None
    cap: str | None = None
    comune_residenza_id: int | None = None
    stato_residenza_id: int | None = None
    cittadinanza_id: int | None = None
    stato_civile_id: int | None = None
    professione_id: int | None = None
    posizione_professionale_id: int | None = None
    livello_istruzione_id: int | None = None
    categoria_paziente_id: int | None = None
    tipo_documento_id: int | None = None
    documento: str | None = None
    data_rilascio: date | None = None
    ente_rilascio: str | None = None
    medico_curante_id: int | None = None
    asp_residenza_id: int | None = None
    presidio_id: int | None = None
    operatore_id: int | None = None
    tessera_team: str | None = None
    peso: float | None = None
    altezza: int | None = None
    num_ist_team: str | None = None
    ente_rilascio_eni_stp: str | None = None
    data_rilascio_eni_stp: date | None = None
    data_scadenza_team_eni_stp: date | None = None
    diniego_fse: bool = False
    nega_presenza_allergie: bool = False
    nega_presenza_patologie: bool = False
    nega_presenza_patologie_infettive: bool = False


class ContattoPzReadMixin(ContattoPzBase):
    """Aggiunge a ContattoPzBase i campi calcolati (IMC, superficie corporea) -
    da comporre insieme a ContattoPzBase nei Read schema dei sottotipi."""

    @computed_field
    @property
    def imc(self) -> float | None:
        if not self.peso or not self.altezza:
            return None
        return round(self.peso / (self.altezza / 100) ** 2, 3)

    @computed_field
    @property
    def superficie_corporea(self) -> float | None:
        if not self.peso or not self.altezza:
            return None
        return round((self.peso**0.425) * (self.altezza**0.725) * 0.007184, 3)
