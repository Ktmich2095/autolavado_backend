import models.Rol
from sqlalchemy.orm import Session
def get_rol(db: Session, skip: int =0, limit: int =10  ):
    return db.query(models.rol.Rol).offset(skip).limit(limit).all()



    