'''Esta clase permite generar el modelo para los tipos de rol'''

from sqlalchemy import Column, Integer, String, Boolean,DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    '''Clase para especificar tabla de usuarios'''
    __tablename__ = "tbc_users"

    Id =Column(Integer, primary_key=True, index=True)
    Rol_Id = Column(Integer, foreignKey("tbc_roles.Id"))
    nombreRol = Column(String(50))
    primerApellido = Column(String(50))
    Correo_Electronico = Column(String(100), unique=True, index=True)
    Contraseña = Column(String(100))    
    Numero_Telefonico = Column(String(15))
    estado = Column(Enum('activo', 'inactivo', name='estado_enum'), default='activo')
    fecha_Registro = Column(DateTime)
    fecha_Actualizacion = Column(DateTime)