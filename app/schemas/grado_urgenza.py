from pydantic import BaseModel, ConfigDict


class GradoUrgenzaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    grado_urgenza: str
    colore: int | None = None
