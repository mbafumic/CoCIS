from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, computed_field


class DipendenteBase(BaseModel):
    cognome: str
    nome: str
    data_nascita: date | None = None
    sesso: Literal["M", "F"] | None = None
    comune_nascita_id: int | None = None
    codice_fiscale: str | None = None
    partita_iva: str | None = None
    comune_residenza_id: int | None = None
    indirizzo: str | None = None
    telefono: str | None = None
    cellulare: str | None = None
    rapporto_dipendenza_id: int | None = None
    data_inizio_rapporto: date | None = None
    data_fine_rapporto: date | None = None
    badge: str | None = None
    sigla: str | None = None
    titolo_id: int | None = None
    tipo_dipendente_id: int | None = None
    presidio_id: int | None = None
    reparto_predefinito_id: int | None = None
    email: str | None = None
    utente_email: str | None = None
    password_email: str | None = None
    pec: str | None = None
    elenco_globale: bool | None = None
    documentix_sezione: bool | None = None
    mostra_ricoveri: bool | None = None
    mostra_sala_operatoria: bool | None = None
    richiesta_emocomponenti: bool | None = None
    segreteria: bool = False
    no_intestazione_referti_amb: bool = False
    presenza_omonimo: bool = False
    avvisato: bool = False
    tipo_firma: Literal["Standard", "DigitaleLocale", "DigitaleRemota"] | None = None
    stato_fse: Literal["SoloFirma", "SoloInvio", "InvioEFirma"] | None = None
    password_changed_at: datetime | None = None
    tipo_rilevazione_inventario: Literal["Umi", "Cnf"] | None = None
    pin_web: str | None = None
    nodo_startup: str | None = None
    codice_esterno: int | None = None
    id_esterno: int | None = None
    avviso: str | None = None


class DipendenteCreate(DipendenteBase):
    pass


class DipendenteRead(DipendenteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    tipo_personale: str

    @computed_field
    @property
    def nominativo(self) -> str:
        return f"{self.cognome} {self.nome}"
