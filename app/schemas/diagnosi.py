from pydantic import BaseModel, ConfigDict


class DiagnosiRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    descrizione: str | None = None
    abbreviazione: str | None = None
    icd9_cm_id: int | None = None
