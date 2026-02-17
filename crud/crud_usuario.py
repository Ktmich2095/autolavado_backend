from sqlalchemy.orm import Session
from passlib.context import CryptContext
import models.model_usuario as model
import schemas.schema_usuario as schema_usuario

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Usuario).offset(skip).limit(limit).all()

def get_usuario_by_nombre(db: Session, nombre: str):
    return db.query(model.Usuario).filter(model.Usuario.nombre == nombre).first()

def get_usuario_by_id(db: Session, usuario_id: int):
    return db.query(model.Usuario).filter(model.Usuario.id == usuario_id).first()

def get_usuario_por_correo(db: Session, correo: str):
    return db.query(model.Usuario).filter(model.Usuario.correo_electronico == correo).first()

def create_usuario(db: Session, usuario: schema_usuario.UsuarioCreate):
    password_plana = usuario.contrasena.strip()
    hashed_password = pwd_context.hash(password_plana)
    db_usuario=models.model_usuario.Usuario(
        rol_id=usuario.rol_id,
        nombre=usuario.nombre,
        primer_apellido=usuario.primer_apellido,
        segundo_apellido=usuario.segundo_apellido,
        direccion=usuario.direccion,
        correo_electronico=usuario.correo_electronico,
        numero_telefono=usuario.numero_telefono,
        contrasena=hashed_password,
        estado=usuario.estado,
        fecha_registro=usuario.fecha_registro,
        fecha_actualizacion=usuario.fecha_actualizacion
    )

    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

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


def verificar_contrasena(password_plana: str, hashed_password: str) -> bool:
    try:
        return pwd_context.verify(password_plana, hashed_password)
    except Exception:
        return False