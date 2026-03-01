from sqlalchemy.orm import Session
from models.model_vehiculo_servicio_usuario import VehiculoServicio
from schemas.schema_vehiculo_servicio import VehiculoServicioCreate, VehiculoServicioUpdate
from datetime import datetime

def crear_asignacion(db: Session, data: VehiculoServicioCreate):
    nueva_asignacion = VehiculoServicio(
        auto_Id=data.auto_Id,
        cajero_Id=data.cajero_Id,
        operador_Id=data.operador_Id,
        servicio_id=data.servicio_id,
        fecha=data.fecha,
        hora=data.hora,
        estatus=data.estatus,
        estado=data.estado
    )
    db.add(nueva_asignacion)
    db.commit()
    db.refresh(nueva_asignacion)
    return nueva_asignacion

def get_asignaciones(db: Session):
    return db.query(VehiculoServicio).all()

def get_asignacion(db: Session, id: int):
    return db.query(VehiculoServicio).filter(VehiculoServicio.Id == id).first()

def delete_asignacion(db: Session, id: int):
    asignacion = get_asignacion(db, id)
    if not asignacion:
        return None
    db.delete(asignacion)
    db.commit()
    return asignacion

def update_asignacion(db: Session, id: int, datos: VehiculoServicioUpdate):
    asignacion = get_asignacion(db, id)
    if not asignacion:
        return None

    for key, value in datos.dict(exclude_unset=True).items():
        setattr(asignacion, key, value)

    asignacion.fecha_actualizacion = datetime.now()
    db.commit()
    db.refresh(asignacion)
    return asignacion