from sqlalchemy.orm import Session
from models.servicio import Servicio
from schemas.schema_servicio import ServicioCreate, ServicioUpdate
from datetime import datetime


# Crear
def create_servicio(db: Session, servicio: ServicioCreate):
    nuevo = Servicio(**servicio.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


# Obtener todos
def get_servicios(db: Session):
    return db.query(Servicio).all()


# Obtener por ID
def get_servicio(db: Session, servicio_id: int):
    return db.query(Servicio).filter(Servicio.Id == servicio_id).first()


# Actualizar
def update_servicio(db: Session, servicio_id: int, datos: ServicioUpdate):
    servicio = get_servicio(db, servicio_id)
    if not servicio:
        return None

    for key, value in datos.dict(exclude_unset=True).items():
        setattr(servicio, key, value)

    servicio.fecha_actualizacion = datetime.now()
    db.commit()
    db.refresh(servicio)
    return servicio


# Eliminar
def delete_servicio(db: Session, servicio_id: int):
    servicio = get_servicio(db, servicio_id)
    if not servicio:
        return None

    db.delete(servicio)
    db.commit()
    return servicio