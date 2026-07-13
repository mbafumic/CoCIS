from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict


class RicoveroBase(BaseModel):
    reparto: str
    data_ricovero: date
    data_dimissione: date | None = None
    stato: Literal["aperto", "dimesso"] = "aperto"


class RicoveroCreate(RicoveroBase):
    pass


class RicoveroRead(RicoveroBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    paziente_id: int
    tipo_contatto: str
    data_apertura: date
