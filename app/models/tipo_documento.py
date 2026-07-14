from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class TipoDocumento(Base):
    __tablename__ = "tipi_documento"

    id: Mapped[int] = mapped_column(primary_key=True)
    tipo_documento: Mapped[str] = mapped_column(String(20))
