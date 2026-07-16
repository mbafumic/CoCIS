from pydantic import BaseModel, ConfigDict, computed_field


class MedicoEsternoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    cognome: str | None = None
    nome: str | None = None
    indirizzo: str | None = None
    telefono: str | None = None
    cellulare: str | None = None
    citta_id: int | None = None
    codice_regionale: str | None = None
    n_empam: str | None = None
    asp_id: int | None = None
    specializzazione: str | None = None
    codice_fiscale: str | None = None
    codice_altro_sistema: int | None = None

    @computed_field
    @property
    def nominativo(self) -> str:
        if not self.nome:
            return self.cognome or ""
        return f"{self.cognome} {self.nome}"
