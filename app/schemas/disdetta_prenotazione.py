from pydantic import BaseModel, ConfigDict


class DisdettaPrenotazioneRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    motivo: str | None = None
    prenotazione_id: int | None = None
