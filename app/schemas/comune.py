from pydantic import BaseModel, ConfigDict, computed_field

from app.schemas.regione import RegioneRead


class ComuneRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    comune: str
    istat: str | None = None
    provincia: str | None = None
    regione: RegioneRead | None = None
    prefisso: str | None = None
    cap: str | None = None
    cod_fisco: str | None = None
    abitanti: int | None = None

    @computed_field
    @property
    def comune_provincia(self) -> str:
        base = f"{self.comune} - {self.provincia}"
        if self.regione is not None:
            base += f" - {self.regione.regione}"
        return base

    @computed_field
    @property
    def comune_istat(self) -> str:
        return f"{self.comune} - {self.istat}"
