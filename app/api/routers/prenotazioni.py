from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.paziente import Paziente
from app.models.prenotazione import Prenotazione
from app.schemas.prenotazione import PrenotazioneCreate, PrenotazioneRead

router = APIRouter(tags=["prenotazioni"])


@router.post(
    "/pazienti/{paziente_id}/prenotazioni",
    response_model=PrenotazioneRead,
    status_code=status.HTTP_201_CREATED,
)
def crea_prenotazione(
    paziente_id: int, payload: PrenotazioneCreate, db: Session = Depends(get_db)
) -> Prenotazione:
    if db.get(Paziente, paziente_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paziente non trovato")

    dati = payload.model_dump()
    # nel legacy la data prenotazione defaulta a oggi (AfterConstruction);
    # data_apertura del ContattoPz coincide con essa.
    dati["data"] = dati.get("data") or date.today()
    prenotazione = Prenotazione(
        paziente_id=paziente_id,
        tipo_contatto="prenotazione",
        data_apertura=dati["data"],
        **dati,
    )
    db.add(prenotazione)
    db.commit()
    db.refresh(prenotazione)
    return prenotazione


@router.get("/pazienti/{paziente_id}/prenotazioni", response_model=list[PrenotazioneRead])
def lista_prenotazioni(paziente_id: int, db: Session = Depends(get_db)) -> list[Prenotazione]:
    stmt = select(Prenotazione).where(Prenotazione.paziente_id == paziente_id)
    return list(db.scalars(stmt))


@router.get("/prenotazioni/{prenotazione_id}", response_model=PrenotazioneRead)
def leggi_prenotazione(prenotazione_id: int, db: Session = Depends(get_db)) -> Prenotazione:
    prenotazione = db.get(Prenotazione, prenotazione_id)
    if prenotazione is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Prenotazione non trovata"
        )
    return prenotazione
