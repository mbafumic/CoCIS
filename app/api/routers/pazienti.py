from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.paziente import Paziente
from app.schemas.paziente import PazienteCreate, PazienteRead

router = APIRouter(prefix="/pazienti", tags=["pazienti"])


@router.post("", response_model=PazienteRead, status_code=status.HTTP_201_CREATED)
def crea_paziente(payload: PazienteCreate, db: Session = Depends(get_db)) -> Paziente:
    paziente = Paziente(**payload.model_dump())
    db.add(paziente)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Codice fiscale già registrato",
        ) from exc
    db.refresh(paziente)
    return paziente


@router.get("/{paziente_id}", response_model=PazienteRead)
def leggi_paziente(paziente_id: int, db: Session = Depends(get_db)) -> Paziente:
    paziente = db.get(Paziente, paziente_id)
    if paziente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paziente non trovato")
    return paziente
