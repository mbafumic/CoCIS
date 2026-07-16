from pydantic import BaseModel, ConfigDict


class TitoloRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    titolo: str
