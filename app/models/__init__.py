from app.db import Base
from app.models.contatto_pz import ContattoPz
from app.models.paziente import Paziente
from app.models.ricovero import Ricovero

__all__ = ["Base", "Paziente", "ContattoPz", "Ricovero"]
