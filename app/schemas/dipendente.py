from pydantic import BaseModel, ConfigDict


class DipendenteRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome: str
    cognome: str
