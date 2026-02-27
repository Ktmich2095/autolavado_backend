from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

import config.db, crud.crud_usuario, schemas.schema_usuario, models.model_usuario
from config.security import create_access_token, get_current_user

usuario = APIRouter()

models.model_usuario.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET Usuarios (requiere token)
@usuario.get("/usuario/", response_model=List[schemas.schema_usuario.Usuario])
def read_usuarios(skip: int = 0, limit: int = 100,
                  db: Session = Depends(get_db),
                  current_user: str = Depends(get_current_user)):
    return crud.crud_usuario.get_usuario(db, skip, limit)

# CREATE Usuario (no requiere token)
@usuario.post("/usuario/", response_model=schemas.schema_usuario.Usuario)
def create_usuario(usuario_data: schemas.schema_usuario.UsuarioCreate, db: Session = Depends(get_db)):
    if crud.crud_usuario.get_usuario_by_nombre(db, usuario_data.nombre):
        raise HTTPException(status_code=400, detail="Usuario existente")
    return crud.crud_usuario.create_usuario(db, usuario_data)

# LOGIN
@usuario.post("/login/")
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    usuario_db = crud.crud_usuario.authenticate_user(db, form_data.username, form_data.password)
    if not usuario_db:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")
    token = create_access_token({"sub": usuario_db.correo_electronico})
    return {"access_token": token, "token_type": "bearer"}