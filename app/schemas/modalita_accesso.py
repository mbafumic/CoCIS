from pydantic import BaseModel, ConfigDict


class ModalitaAccessoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    modalita: str
