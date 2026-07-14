from pydantic import BaseModel, ConfigDict, computed_field

from app.schemas.regione import RegioneRead


class AspRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    azienda: str | None = None
    denominazione: str | None = None
    indirizzo: str | None = None
    cap: str | None = None
    citta_id: int | None = None
    regione: RegioneRead | None = None
    anno: int | None = None
    partita_iva: str | None = None

    @computed_field
    @property
    def codice_denominazione(self) -> str:
        base = f"{self.azienda} - {self.denominazione}"
        if self.regione is not None:
            base += f" - {self.regione.regione}"
        return base
