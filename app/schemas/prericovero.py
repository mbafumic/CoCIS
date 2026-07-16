from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict

from app.schemas.contatto_pz import ContattoPzBase, ContattoPzReadMixin
from app.schemas.prenotazione import RegimeRicovero

Mese = Literal[
    "Gennaio",
    "Febbraio",
    "Marzo",
    "Aprile",
    "Maggio",
    "Giugno",
    "Luglio",
    "Agosto",
    "Settembre",
    "Ottobre",
    "Novembre",
    "Dicembre",
]


class PrericoveroBase(BaseModel):
    regime_ricovero: RegimeRicovero | None = None
    disciplina_ricovero_id: int | None = None
    data_inizio: date | None = None
    data_fine: date | None = None
    cartella_clinica: int | None = None
    modalita_accesso_id: int | None = None
    scheda_e: bool | None = None
    codice_impegnativa: str | None = None
    numero_impegnativa: str | None = None
    data_impegnativa: date | None = None
    provenienza_id: int | None = None
    diagnosi_ingresso_id: int | None = None
    medico_inviante_id: int | None = None
    prenotazione_id: int | None = None
    locked_user_id: int | None = None
    specialista_medico_id: int | None = None
    specialista_chirurgo_id: int | None = None
    tutor_id: int | None = None
    parente_id: int | None = None
    note_amministrative: str | None = None
    note_cliniche: str | None = None
    computer: str | None = None
    anno_prericovero: int | None = None
    mese_prericovero: Mese | None = None


class PrericoveroCreate(ContattoPzBase, PrericoveroBase):
    pass


class PrericoveroRead(ContattoPzReadMixin, PrericoveroBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    paziente_id: int
    tipo_contatto: str
    data_apertura: date
