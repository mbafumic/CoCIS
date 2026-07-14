from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict, computed_field


class PazienteBase(BaseModel):
    nome: str
    cognome: str
    data_nascita: date
    codice_fiscale: str
    sesso: Literal["M", "F"] | None = None
    eta: str | None = None
    luogo_nascita_id: int | None = None
    gruppo_sanguigno_id: int | None = None
    deceduto: bool | None = None
    testimone_di_geova: bool | None = None
    telefoni_paziente: str | None = None
    telefoni_parenti: str | None = None
    consenso_tratt_pers: bool = False
    consenso_dossier: bool = False
    download_referti: str | None = None
    codice_esterno: int | None = None


class PazienteCreate(PazienteBase):
    pass


class PazienteRead(PazienteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int

    @computed_field
    @property
    def nominativo(self) -> str:
        return f"{self.cognome.strip()} {self.nome.strip()}"

    @computed_field
    @property
    def iniziali(self) -> str:
        iniziali = "".join(f"{parola[0]}." for parola in self.cognome.split() if parola)
        iniziali += " "
        iniziali += "".join(f"{parola[0]}." for parola in self.nome.split() if parola)
        return iniziali
