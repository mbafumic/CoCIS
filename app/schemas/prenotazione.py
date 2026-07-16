from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict

from app.schemas.contatto_pz import ContattoPzBase, ContattoPzReadMixin

RegimeRicovero = Literal["Ordinario", "DHDS", "DayService", "PreRicovero", "PreRicoveroDH"]


class PrenotazioneBase(BaseModel):
    data: date | None = None
    regime_ricovero: RegimeRicovero | None = None
    data_prevista_ricovero: date | None = None
    ora_ricovero: datetime | None = None
    data_prev_pre_ric: date | None = None
    data_tampone: date | None = None
    grado_urgenza_id: int | None = None
    unita_funzionale_id: int | None = None
    diagnosi_ingresso_id: int | None = None
    modalita_accesso_id: int | None = None
    medico_inviante_id: int | None = None
    specialista_medico_id: int | None = None
    specialista_chirurgo_id: int | None = None
    tutor_id: int | None = None
    note_amministrative: str | None = None
    note_cliniche: str | None = None
    classe_priorita: Literal["A", "B", "C", "D"] | None = None
    motivo_dh: Literal["Diagnostico", "Chirurgico", "Terapeutico", "Riabilitativo"] | None = None
    stato: Literal["DaEvadere", "Evasa", "Bloccata", "Disdetta", "EvasoPreric"] | None = None
    bloccato: bool | None = None
    data_blocco: date | None = None
    email: str | None = None
    camera_singola: bool = False
    data_avviso: date | None = None
    avvisato: bool = False


class PrenotazioneCreate(ContattoPzBase, PrenotazioneBase):
    pass


class PrenotazioneRead(ContattoPzReadMixin, PrenotazioneBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    paziente_id: int
    tipo_contatto: str
    data_apertura: date
