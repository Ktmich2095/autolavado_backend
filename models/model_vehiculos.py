from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from config.db import Base
from datetime import datetime

class Vehiculo(Base):
    __tablename__ = "tbc_vehiculos"

    id = Column("Id", Integer, primary_key=True, index=True)
    usuario_id = Column("usuario_Id", Integer, ForeignKey("tbb_usuarios.Id"))

    modelo = Column(String(45), nullable=False)
    marca = Column(String(45), nullable=False)
    placa = Column(String(45), nullable=False, unique=True)
    serie = Column(String(45), nullable=True)
    color = Column(String(45), nullable=True)
    tipo = Column(String(45), nullable=True)
    anio = Column(Integer, nullable=True)

    estatus = Column(Boolean, default=True)

    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
