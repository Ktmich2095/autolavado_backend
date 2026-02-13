from sqlalchemy import Column, Integer, String,Boolean,Float,DateTime
# from sqlalchemy.orm import relationship
from sqlalchemy import DECIMAL

from config.db import Base

class Servicio(Base):
    __tablename__ = "c_servicio"

    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(80))
    descripcion = Column(String(850))
    costo = Column(DECIMAL(18,2))
    duracion= Column(Integer)
    estado = Column(Boolean)
    fecha_registro= Column(DateTime)
    fecha_actualizacion= Column(DateTime)