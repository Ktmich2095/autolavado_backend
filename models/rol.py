'''Esta clase permite generar el modelo para los tipos de rol'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.db import Base

class Rol(Base):
    
    ''' Creacion de la tabla de roles en Mysql'''
    __tablename__ = "c_rol"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(45), nullable=False)

    estado = Column(Boolean)
    # usuarios = relationship("Usuario", back_populates="rol")

    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
    
