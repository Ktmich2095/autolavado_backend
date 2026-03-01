from sqlalchemy.orm import Session
from models.user import Usuario
from schemas.schema_usuario import UsuarioCreate, UsuarioUpdate
from config.security import get_password_hash
from datetime import datetime
from fastapi import HTTPException
from models.rol import Rol


def create_usuario(db: Session, usuario: UsuarioCreate):
    # Verificar si el rol existe
    rol = db.query(Rol).filter(Rol.Id == usuario.rol_Id).first()
    if not rol:
        raise HTTPException(status_code=400, detail=f"El rol con ID {usuario.rol_Id} no existe")

    hashed_password = get_password_hash(usuario.password)

    nuevo_usuario = Usuario(
        rol_Id=usuario.rol_Id,
        nombre=usuario.nombre,
        apellidoPaterno=usuario.apellidoPaterno,
        apellidoMaterno=usuario.apellidoMaterno,
        direccion=usuario.direccion,
        correo_electronico=usuario.correo_electronico,
        numero_telefono=usuario.numero_telefono,
        password=hashed_password,
        estado=usuario.estado
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

# Obtener todos
def get_usuarios(db: Session):
    return db.query(Usuario).all()


def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.Id == usuario_id).first()


def get_usuario_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.correo_electronico == email).first()


def update_usuario(db: Session, usuario_id: int, datos: UsuarioUpdate):
    usuario = get_usuario(db, usuario_id)
    if not usuario:
        return None

    for key, value in datos.dict(exclude_unset=True).items():
        setattr(usuario, key, value)

    usuario.fecha_actualizacion = datetime.now()
    db.commit()
    db.refresh(usuario)
    return usuario


def delete_usuario(db: Session, usuario_id: int):
    usuario = get_usuario(db, usuario_id)
    if not usuario:
        return None

    db.delete(usuario)
    db.commit()
    return usuario