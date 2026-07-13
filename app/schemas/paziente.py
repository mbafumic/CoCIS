from datetime import date

from pydantic import BaseModel, ConfigDict


class PazienteBase(BaseModel):
    nome: str
    cognome: str
    data_nascita: date
    codice_fiscale: str


class PazienteCreate(PazienteBase):
    pass


class PazienteRead(PazienteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
