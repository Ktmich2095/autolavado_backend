from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from schemas.schema_servicio import (
    ServicioCreate,
    ServicioUpdate,
    ServicioResponse
)
from typing import List
from crud import crud_servicios
from config.security import get_current_user

router = APIRouter(
    prefix="/servicios",
    tags=["Servicios"],
    dependencies=[Depends(get_current_user)]  # 🔒
)

@router.post("/", response_model=ServicioResponse)
def crear_servicio(servicio: ServicioCreate, db: Session = Depends(get_db)):
    return crud_servicios.create_servicio(db, servicio)


@router.get("/", response_model=List[ServicioResponse])
def obtener_servicios(db: Session = Depends(get_db)):
    return crud_servicios.get_servicios(db)


@router.get("/{servicio_id}", response_model=ServicioResponse)
def obtener_servicio(servicio_id: int, db: Session = Depends(get_db)):
    servicio = crud_servicios.get_servicio(db, servicio_id)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio


@router.put("/{servicio_id}", response_model=ServicioResponse)
def actualizar_servicio(servicio_id: int, datos: ServicioUpdate, db: Session = Depends(get_db)):
    servicio = crud_servicios.update_servicio(db, servicio_id, datos)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio


@router.delete("/{servicio_id}")
def eliminar_servicio(servicio_id: int, db: Session = Depends(get_db)):
    servicio = crud_servicios.delete_servicio(db, servicio_id)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return {"mensaje": "Servicio eliminado correctamente"}