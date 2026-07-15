from pydantic import BaseModel, ConfigDict


class TipoDipendenteRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    tipo: str
