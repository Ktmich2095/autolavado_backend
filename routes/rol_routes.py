from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from schemas.schema_rol import RolCreate, RolResponse
from typing import List
from crud import crud_rol
from config.security import get_current_user

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
    dependencies=[Depends(get_current_user)]  # 🔒
)


@router.post("/", response_model=RolResponse)
def crear_rol(rol: RolCreate, db: Session = Depends(get_db)):
    return crud_rol.create_rol(db, rol)


@router.get("/", response_model=List[RolResponse])
def obtener_roles(db: Session = Depends(get_db)):
    return crud_rol.get_roles(db)


@router.get("/{rol_id}", response_model=RolResponse)
def obtener_rol(rol_id: int, db: Session = Depends(get_db)):
    rol = crud_rol.get_rol(db, rol_id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol


@router.put("/{rol_id}", response_model=RolResponse)
def actualizar_rol(rol_id: int, datos: RolCreate, db: Session = Depends(get_db)):
    rol = crud_rol.update_rol(db, rol_id, datos)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol


@router.delete("/{rol_id}")
def eliminar_rol(rol_id: int, db: Session = Depends(get_db)):
    rol = crud_rol.delete_rol(db, rol_id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return {"mensaje": "Rol eliminado correctamente"}