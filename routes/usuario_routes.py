from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import Usuario
from config.db import get_db
from schemas.schema_usuario import (
    UsuarioCreate,
    UsuarioUpdate,
    UsuarioResponse
)
from fastapi.security import OAuth2PasswordRequestForm
from config.security import verify_password, create_access_token, get_current_user
from typing import List
from crud import crud_usuarios

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

# 🔓 Crear usuario libre
@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return crud_usuarios.create_usuario(db, usuario)


# 🔐 Login libre
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = crud_usuarios.get_usuario_by_email(db, form_data.username)

    if not usuario or not verify_password(form_data.password, usuario.password):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    access_token = create_access_token(
        data={"sub": str(usuario.Id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# 🔒 Todo lo demás protegido
@router.get("/", response_model=List[UsuarioResponse], dependencies=[Depends(get_current_user)])
def obtener_usuarios(db: Session = Depends(get_db)):
    return crud_usuarios.get_usuarios(db)


@router.get("/{usuario_id}", response_model=UsuarioResponse, dependencies=[Depends(get_current_user)])
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud_usuarios.get_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.put("/{usuario_id}", response_model=UsuarioResponse, dependencies=[Depends(get_current_user)])
def actualizar_usuario(usuario_id: int, datos: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = crud_usuarios.update_usuario(db, usuario_id, datos)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.delete("/{usuario_id}", dependencies=[Depends(get_current_user)])
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud_usuarios.delete_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado correctamente"}