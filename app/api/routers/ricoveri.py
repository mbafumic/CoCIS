from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.paziente import Paziente
from app.models.ricovero import Ricovero
from app.schemas.ricovero import RicoveroCreate, RicoveroRead

router = APIRouter(tags=["ricoveri"])


@router.post(
    "/pazienti/{paziente_id}/ricoveri",
    response_model=RicoveroRead,
    status_code=status.HTTP_201_CREATED,
)
def crea_ricovero(
    paziente_id: int, payload: RicoveroCreate, db: Session = Depends(get_db)
) -> Ricovero:
    if db.get(Paziente, paziente_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paziente non trovato")

    ricovero = Ricovero(
        paziente_id=paziente_id,
        tipo_contatto="ricovero",
        data_apertura=payload.data_ricovero,
        **payload.model_dump(),
    )
    db.add(ricovero)
    db.commit()
    db.refresh(ricovero)
    return ricovero


@router.get("/pazienti/{paziente_id}/ricoveri", response_model=list[RicoveroRead])
def lista_ricoveri(paziente_id: int, db: Session = Depends(get_db)) -> list[Ricovero]:
    stmt = select(Ricovero).where(Ricovero.paziente_id == paziente_id)
    return list(db.scalars(stmt))


@router.get("/ricoveri/{ricovero_id}", response_model=RicoveroRead)
def leggi_ricovero(ricovero_id: int, db: Session = Depends(get_db)) -> Ricovero:
    ricovero = db.get(Ricovero, ricovero_id)
    if ricovero is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ricovero non trovato")
    return ricovero
