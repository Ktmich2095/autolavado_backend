from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from config.db import Base
from datetime import datetime


class Usuario(Base):
    __tablename__ = "tbb_usuarios"

    id = Column("Id", Integer, primary_key=True, index=True)
    rol_id = Column("rol_Id", Integer, ForeignKey("tbc_roles.Id"))

    nombre = Column(String(60), nullable=False)
    primer_apellido = Column(String(60), nullable=False)
    segundo_apellido = Column(String(60), nullable=True)
    direccion = Column(String(200), nullable=True)
    correo_electronico = Column(String(100), nullable=False, unique=True)
    numero_telefono = Column(String(20), nullable=True)
    contrasena = Column(String(60), nullable=False)

    estatus = Column(Boolean, default=True)

    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
