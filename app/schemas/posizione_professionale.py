from pydantic import BaseModel, ConfigDict


class PosizioneProfessionaleRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    posizione: str
