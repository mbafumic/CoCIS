from pydantic import BaseModel, ConfigDict


class TipoDocumentoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    tipo_documento: str
