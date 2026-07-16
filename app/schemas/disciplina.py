from pydantic import BaseModel, ConfigDict


class DisciplinaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    codice: str | None = None
    disciplina: str | None = None
    attiva: bool | None = None
    trasferimento_interno: bool | None = None
    standard_procedure: str | None = None
    gg_terapia_fino_sosp: int | None = None
    allegati_cc: bool | None = None
    responsabile_id: int | None = None
    reparto_degenza_id: int | None = None
