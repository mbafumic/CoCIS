from pydantic import BaseModel, ConfigDict


class PresidioOspRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    presidio: str | None = None
    comune_id: int | None = None
    indirizzo: str | None = None
    cap: str | None = None
    prov: str | None = None
    tel: str | None = None
    fax: str | None = None
    email: str | None = None
