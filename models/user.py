'''Esta clase permite generar el modelo para los tipos de user'''
from sqlalchemy import Column, Integer, String,Boolean,Float,DateTime,ForeignKey
# from sqlalchemy.orm import relationship
from config.db import Base

class Usuario(Base):
    __tablename__ = "c_usuario"

    Id = Column(Integer, primary_key=True, index=True)
    ro_Id = Column(Integer, ForeignKey("c_rol.id"))
    nombre = Column(String(60))
    apellidoPaterno = Column(String(60))
    apellidoMaterno = Column(String(60))
    direccion = Column(String(200))
    correo_electronico= Column(String(100))
    numero_telefono= Column(String(20))
    password = Column(String(256))

    estatus= Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
