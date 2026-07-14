from pydantic import BaseModel, ConfigDict


class CategoriaPazienteRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    categoria: str
