'''Esta clase permite generar el modelo para los tipos de rol'''

from sqlalchemy import Column, Integer, String, Boolean,DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class Rol(Base):
    '''Clase para especificar tabla de usuarios'''
    __tablename__ = "tbc_roles"

    Id =Column(Integer, primary_key=True, index=True)
    nombreRol = Column(String(50))
    estado = Column(Boolean)