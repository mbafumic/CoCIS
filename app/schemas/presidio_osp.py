from pydantic import BaseModel, ConfigDict


class PresidioOspRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    presidio: str | None = None
    comune_id: int | None = None
    indirizzo: str | None = None
    cap: str | None = None
    tel: str | None = None
    fax: str | None = None
    email: str | None = None
    asp_id: int | None = None
    header: str | None = None
    footer: str | None = None
    header_fattura: str | None = None
    header_clinico: str | None = None
    smtp: str | None = None
    mail_host: str | None = None
    smtp_port: int | None = None
    direttore_sanitario_id: int | None = None
    responsabile_dipartimento_id: int | None = None
