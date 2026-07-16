from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.paziente import Paziente
from app.models.prericovero import Prericovero
from app.schemas.prericovero import PrericoveroCreate, PrericoveroRead

router = APIRouter(tags=["prericoveri"])


@router.post(
    "/pazienti/{paziente_id}/prericoveri",
    response_model=PrericoveroRead,
    status_code=status.HTTP_201_CREATED,
)
def crea_prericovero(
    paziente_id: int, payload: PrericoveroCreate, db: Session = Depends(get_db)
) -> Prericovero:
    if db.get(Paziente, paziente_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paziente non trovato")

    dati = payload.model_dump()
    dati["data_inizio"] = dati.get("data_inizio") or date.today()
    prericovero = Prericovero(
        paziente_id=paziente_id,
        tipo_contatto="prericovero",
        data_apertura=dati["data_inizio"],
        **dati,
    )
    db.add(prericovero)
    db.commit()
    db.refresh(prericovero)
    return prericovero


@router.get("/pazienti/{paziente_id}/prericoveri", response_model=list[PrericoveroRead])
def lista_prericoveri(paziente_id: int, db: Session = Depends(get_db)) -> list[Prericovero]:
    stmt = select(Prericovero).where(Prericovero.paziente_id == paziente_id)
    return list(db.scalars(stmt))


@router.get("/prericoveri/{prericovero_id}", response_model=PrericoveroRead)
def leggi_prericovero(prericovero_id: int, db: Session = Depends(get_db)) -> Prericovero:
    prericovero = db.get(Prericovero, prericovero_id)
    if prericovero is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prericovero non trovato")
    return prericovero
