from pydantic import BaseModel, ConfigDict


class RegioneRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    regione: str
    codice: str | None = None
    ordine_stampa: int | None = None
