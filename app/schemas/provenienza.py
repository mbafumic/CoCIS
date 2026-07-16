from pydantic import BaseModel, ConfigDict


class ProvenienzaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    provenienza: str
    anno_inizio_validita: int | None = None
    anno_fine_validita: int | None = None
