from sqlalchemy.orm import Session
from passlib.context import CryptContext
from passlib.exc import UnknownHashError
import models.model_usuario, schemas.schema_usuario

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def get_usuario(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.model_usuario.Usuario).offset(skip).limit(limit).all()

def get_usuario_by_nombre(db: Session, nombre: str):
    return db.query(models.model_usuario.Usuario).filter(models.model_usuario.Usuario.nombre == nombre).first()

def create_usuario(db: Session, usuario: schemas.schema_usuario.UsuarioCreate):
    hashed_password = pwd_context.hash(usuario.contrasena)
    db_usuario = models.model_usuario.Usuario(
        rol_Id=usuario.rol_Id,
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

def authenticate_user(db: Session, email_o_tel: str, contrasena: str):
    usuario = db.query(models.model_usuario.Usuario).filter(
        (models.model_usuario.Usuario.correo_electronico == email_o_tel) |
        (models.model_usuario.Usuario.numero_telefono == email_o_tel)
    ).first()
    if not usuario:
        return None
    try:
        if not pwd_context.verify(contrasena, usuario.contrasena):
            return None
    except UnknownHashError:
        return None
    return usuario