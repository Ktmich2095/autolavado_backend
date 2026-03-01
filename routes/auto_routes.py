from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from schemas.schema_auto import AutoCreate, AutoUpdate, AutoResponse
from typing import List
from crud import crud_vehiculo
from config.security import get_current_user

router = APIRouter(
    prefix="/autos",
    tags=["Autos"],
    dependencies=[Depends(get_current_user)]  # 🔒 Protegido
)


@router.post("/", response_model=AutoResponse)
def crear_auto(auto: AutoCreate, db: Session = Depends(get_db)):
    return crud_vehiculo.create_auto(db, auto)


@router.get("/", response_model=List[AutoResponse])
def obtener_autos(db: Session = Depends(get_db)):
    return crud_vehiculo.get_autos(db)


@router.get("/{auto_id}", response_model=AutoResponse)
def obtener_auto(auto_id: int, db: Session = Depends(get_db)):
    auto = crud_vehiculo.get_auto(db, auto_id)
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return auto


@router.put("/{auto_id}", response_model=AutoResponse)
def actualizar_auto(auto_id: int, datos: AutoUpdate, db: Session = Depends(get_db)):
    auto = crud_vehiculo.update_auto(db, auto_id, datos)
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return auto


@router.delete("/{auto_id}")
def eliminar_auto(auto_id: int, db: Session = Depends(get_db)):
    auto = crud_vehiculo.delete_auto(db, auto_id)
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return {"mensaje": "Auto eliminado correctamente"}