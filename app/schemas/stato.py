from pydantic import BaseModel, ConfigDict, computed_field


class StatoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    stato: str
    codice_istat: str | None = None
    nazionalita: str | None = None
    codice_iso: str | None = None
    comunitario: bool | None = None

    @computed_field
    @property
    def istat_stato(self) -> str:
        return f"{self.codice_istat} - {self.stato}"
