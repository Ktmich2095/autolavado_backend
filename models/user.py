'''Esta clase permite generar el modelo para los tipos de user'''
from sqlalchemy import Column, Integer, String,Boolean,Float,DateTime,ForeignKey
# from sqlalchemy.orm import relationship
from config.db import Base

class Usuario(Base):
    __tablename__ = "c_usuario"

    Id = Column(Integer, primary_key=True, index=True)
    rol_Id = Column(Integer, ForeignKey("c_rol.id"))
    nombre = Column(String(60))
    primer_apellido = Column(String(60))
    segundo_apellido = Column(String(60))
    direccion = Column(String(200))
    correo_electronico= Column(String(100))
    numero_telefono= Column(String(20))
    contrasena = Column(String(256))
    estado= Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
