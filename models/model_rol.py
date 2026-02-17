"""Esta clase permite generar el modelo para los tipos de rol"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class Rol(Base):

    __tablename__ = "tbc_roles"

    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(45), nullable=False)
    estatus = Column(Boolean, default=True)

    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    usuarios = relationship("Usuario", back_populates="rols")    
