from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from schemas.schema_vehiculo_servicio import (
    VehiculoServicioCreate,
    VehiculoServicioUpdate,
    VehiculoServicioResponse
)
from typing import List
from crud import crud_vehiculos_servicios_usuarios

from config.security import get_current_user

router = APIRouter(
    prefix="/vehiculo-servicios",
    tags=["Vehiculo Servicios"],
    dependencies=[Depends(get_current_user)]  # 🔒
)
@router.post("/", response_model=VehiculoServicioResponse)
def crear_asignacion(data: VehiculoServicioCreate, db: Session = Depends(get_db)):
    return crud_vehiculos_servicios_usuarios.crear_asignacion(db, data)


@router.get("/", response_model=List[VehiculoServicioResponse])
def obtener_asignaciones(db: Session = Depends(get_db)):
    return crud_vehiculos_servicios_usuarios.get_asignaciones(db)


@router.get("/{id}", response_model=VehiculoServicioResponse)
def obtener_asignacion(id: int, db: Session = Depends(get_db)):
    asignacion = crud_vehiculos_servicios_usuarios.get_asignacion(db, id)
    if not asignacion:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")
    return asignacion


@router.put("/{id}", response_model=VehiculoServicioResponse)
def actualizar_asignacion(id: int, datos: VehiculoServicioUpdate, db: Session = Depends(get_db)):
    asignacion = crud_vehiculos_servicios_usuarios.update_asignacion(db, id, datos)
    if not asignacion:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")
    return asignacion


@router.delete("/{id}")
def eliminar_asignacion(id: int, db: Session = Depends(get_db)):
    asignacion = crud_vehiculos_servicios_usuarios.delete_asignacion(db, id)
    if not asignacion:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")
    return {"mensaje": "Asignación eliminada correctamente"}