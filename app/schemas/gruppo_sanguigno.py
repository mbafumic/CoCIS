from pydantic import BaseModel, ConfigDict


class GruppoSanguignoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    gruppo: str
