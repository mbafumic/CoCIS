from datetime import date
from decimal import Decimal
from typing import Literal

from pydantic import ConfigDict, computed_field

from app.schemas.dipendente import DipendenteBase


class MedicoBase(DipendenteBase):
    """Un Medico è un Dipendente: eredita tutti i campi dell'anagrafica personale."""

    n_empam: str | None = None
    codice_regionale: str | None = None
    codice_lis: str | None = None
    chirurgo: bool = False
    revisore_cc: bool = False
    no_validazione_rilascio: bool = False
    font_referti: str | None = None
    sigla_prog_op: str | None = None
    percentuale_ambulatorio: Decimal | None = None
    percentuale_ambulatorio_prec: Decimal | None = None
    data_variazione_percentuale: date | None = None
    tipo_compenso: Literal["Fattura", "BustaPaga", "Altro"] | None = None
    specializzando: bool = False
    tutor_spec_id: int | None = None
    anno_corso: str | None = None


class MedicoCreate(MedicoBase):
    pass


class MedicoRead(MedicoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    tipo_personale: str

    @computed_field
    @property
    def nominativo(self) -> str:
        return f"{self.cognome} {self.nome}"

    @computed_field
    @property
    def firma_referti(self) -> str:
        nominativo = f"{self.cognome} {self.nome}".strip()
        if self.codice_regionale:
            return f"{nominativo} - {self.codice_regionale}"
        return nominativo
