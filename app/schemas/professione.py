from pydantic import BaseModel, ConfigDict


class ProfessioneRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    professione: str
