from sqlalchemy.orm import Session
import models.model_vehiculos_servicios_usuarios as model


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.AutoServicio)\
        .offset(skip)\
        .limit(limit)\
        .all()


def get_by_id(db: Session, registro_id: int):
    return db.query(model.AutoServicio)\
        .filter(model.AutoServicio.id == registro_id)\
        .first()


def create(db: Session, data):
    nuevo = model.AutoServicio(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def update(db: Session, registro_id: int, data):
    registro = get_by_id(db, registro_id)
    if not registro:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(registro, key, value)

    db.commit()
    db.refresh(registro)
    return registro


def delete(db: Session, registro_id: int):
    registro = get_by_id(db, registro_id)
    if not registro:
        return None

    db.delete(registro)
    db.commit()
    return registro
