from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime


class Servicio(Base):
    __tablename__ = "tbc_servicios"

    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(80), nullable=False)
    descripcion = Column(String(150))
    costo = Column(Float, nullable=False)
    duracion = Column(Integer)
    estado = Column(Boolean, default=True)

    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
