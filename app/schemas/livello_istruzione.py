from pydantic import BaseModel, ConfigDict


class LivelloIstruzioneRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    livello_istruzione: str
