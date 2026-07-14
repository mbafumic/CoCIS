from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Dipendente(Base):
    """Personale della struttura. Versione minima (solo identificazione), usata
    per ora come lookup per l'operatore che apre un ContattoPz. L'anagrafica
    completa del personale (GlobalModule, ruoli/reparti/contratti) è una slice
    futura - vedi mappa dei moduli in CLAUDE.md.
    """

    __tablename__ = "dipendenti"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    cognome: Mapped[str] = mapped_column(String(100))
