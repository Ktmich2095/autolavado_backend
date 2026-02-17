from sqlalchemy.orm import Session
import models.model_usuario as model
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Usuario).offset(skip).limit(limit).all()


def get_usuario_by_id(db: Session, usuario_id: int):
    return db.query(model.Usuario).filter(model.Usuario.id == usuario_id).first()


def get_usuario_por_correo(db: Session, correo: str):
    return db.query(model.Usuario).filter(model.Usuario.correo_electronico == correo).first()


def create_usuario(db: Session, data):
    hashed_password = pwd_context.hash(data.contrasena)
    nuevo = model.Usuario(
        **data.dict(exclude={"contrasena"}),
        contrasena=hashed_password
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def update_usuario(db: Session, usuario_id: int, data):
    usuario = get_usuario_by_id(db, usuario_id)
    if not usuario:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        if key == "contrasena":
            setattr(usuario, key, pwd_context.hash(value))
        else:
            setattr(usuario, key, value)

    db.commit()
    db.refresh(usuario)
    return usuario


def delete_usuario(db: Session, usuario_id: int):
    usuario = get_usuario_by_id(db, usuario_id)
    if not usuario:
        return None

    db.delete(usuario)
    db.commit()
    return usuario
