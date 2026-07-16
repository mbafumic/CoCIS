from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


class RepartoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    reparto: str | None = None
    sigla: str | None = None
    tipo: Literal["Degenza", "Servizio", "Supporto"] | None = None
    presidio_id: int | None = None
    letti_accreditati: int | None = None
    letti_non_accreditati: int | None = None
    no_check_letto_occupato: bool = False
    tipo_magazzino: Literal["Centrale", "Reparto", "Nessuno"] | None = None
    reparto_mag_id: int | None = None
    reparto_trasf_mag_id: int | None = None
    accetta_trasferimenti: bool | None = None
    effettua_procedure: bool | None = None
    gestione_notizie_cliniche: bool | None = None
    gestione_terapia: bool = False
    data_avvio_terapia: date | None = None
    ora_validazione_terapia: datetime | None = None
    max_anticipo_somministrazione: int | None = None
    max_posticipo_somministrazione: int | None = None
    ora_insulina_colazione: datetime | None = None
    ora_insulina_pranzo: datetime | None = None
    ora_insulina_cena: datetime | None = None
    ora_insulina_sera: datetime | None = None
    codice_lis: str | None = None
    diario_fkt: bool = False
    consegne_lavagna: bool = False
    print_order: int | None = None
    standard_procedure_giorno: str | None = None
    standard_procedure_cipi_giorno: str | None = None
    personale_docwin: str | None = None
    shutdown_time: int | None = None
