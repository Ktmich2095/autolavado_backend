'''Esta clase permite generar el modelo para los tipos de user'''
from sqlalchemy import Column, Integer, String,Boolean,Float,DateTime,ForeignKey
# from sqlalchemy.orm import relationship
from config.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
class Usuario(Base):
    __tablename__ = "c_usuario"

    Id = Column(Integer, primary_key=True, index=True)
    rol_Id = Column(Integer, ForeignKey("c_rol.Id"))

    nombre = Column(String(60))
    apellidoPaterno = Column(String(60))
    apellidoMaterno = Column(String(60))
    direccion = Column(String(200))
    correo_electronico = Column(String(100), unique=True)  # recomendado
    numero_telefono = Column(String(20))
    password = Column(String(256))
    estado = Column(Boolean)

    rol = relationship("Rol", back_populates="usuarios")  # === NUEVO ===
    autos = relationship("Auto", back_populates="usuario")  # === NUEVO ===

    fecha_registro = Column(DateTime, default=func.now())
    fecha_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())