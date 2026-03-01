from sqlalchemy.orm import Session
from models.rol import Rol
from schemas.schema_rol import RolCreate


# Crear rol
def create_rol(db: Session, rol: RolCreate):
    nuevo_rol = Rol(**rol.dict())
    db.add(nuevo_rol)
    db.commit()
    db.refresh(nuevo_rol)
    return nuevo_rol


# Obtener todos
def get_roles(db: Session):
    return db.query(Rol).all()


# 🔥 ESTA ES LA QUE TE FALTA
def get_rol(db: Session, rol_id: int):
    return db.query(Rol).filter(Rol.Id == rol_id).first()


# Actualizar
def update_rol(db: Session, rol_id: int, datos: RolCreate):
    rol = db.query(Rol).filter(Rol.Id == rol_id).first()
    if rol:
        for key, value in datos.dict().items():
            setattr(rol, key, value)
        db.commit()
        db.refresh(rol)
    return rol


# Eliminar
def delete_rol(db: Session, rol_id: int):
    rol = db.query(Rol).filter(Rol.Id == rol_id).first()
    if rol:
        db.delete(rol)
        db.commit()
    return rol