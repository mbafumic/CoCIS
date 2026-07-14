from pydantic import BaseModel, ConfigDict


class StatoCivileRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    stato_civile: str
