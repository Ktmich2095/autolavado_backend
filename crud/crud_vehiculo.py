from sqlalchemy.orm import Session
from models.auto import Auto
from schemas.schema_auto import AutoCreate, AutoUpdate
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


def create_auto(db: Session, auto: AutoCreate):
    nuevo = Auto(**auto.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def get_autos(db: Session):
    return db.query(Auto).all()


def get_auto(db: Session, auto_id: int):
    return db.query(Auto).filter(Auto.Id == auto_id).first()


def update_auto(db: Session, auto_id: int, datos: AutoUpdate):
    auto = get_auto(db, auto_id)
    if not auto:
        return None

    for key, value in datos.dict(exclude_unset=True).items():
        setattr(auto, key, value)

    auto.fecha_actualizacion = datetime.now()
    db.commit()
    db.refresh(auto)
    return auto


def delete_auto(db: Session, auto_id: int):
    auto = get_auto(db, auto_id)
    if not auto:
        return None

    try:
        db.delete(auto)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail="No se puede eliminar el auto porque tiene servicios o asignaciones relacionadas."
        )
    return auto