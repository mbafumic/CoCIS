from pydantic import BaseModel, ConfigDict


class RapportoDipendenzaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    rapporto: str
