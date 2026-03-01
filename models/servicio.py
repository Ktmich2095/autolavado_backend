from sqlalchemy import Column, Integer, String,Boolean,Float,DateTime
# from sqlalchemy.orm import relationship
from sqlalchemy import DECIMAL
from sqlalchemy.sql import func
from config.db import Base

class Servicio(Base):
    __tablename__ = "c_servicio"

    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(80))
    descripcion = Column(String(850))
    costo = Column(DECIMAL(18,2))
    duracion_minutos= Column(Integer)
    estado = Column(Boolean)
    fecha_registro = Column(DateTime, default=func.now())
    fecha_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())







    