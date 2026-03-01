''' Esta clase permite generar el modelo para las ventas y asignaciones'''
from sqlalchemy import Column, Integer, Boolean, DateTime, Date, Time, ForeignKey, Enum
from enum import Enum as PyEnum
from config.db import Base
from sqlalchemy.sql import func
class Estatus(PyEnum):
    Programado = "Programado"
    Proceso = "Proceso"
    Realizado = "Realizado"
    Cancelada = "Cancelada"

class VehiculoServicio(Base):
    __tablename__ = "vehiculos_servicios_usuarios"

    Id = Column(Integer, primary_key=True, index=True)
    auto_Id = Column(Integer, ForeignKey("c_auto.Id"), nullable=False)
    cajero_Id = Column(Integer, ForeignKey("c_usuario.Id"))
    operador_Id = Column(Integer, ForeignKey("c_usuario.Id"))
    servicio_id = Column(Integer, ForeignKey("c_servicio.Id"))

    fecha = Column(Date)
    hora = Column(Time)
    estatus = Column(Enum(Estatus), default=Estatus.Programado)
    estado = Column(Boolean)

    fecha_registro = Column(DateTime, default=func.now())
    fecha_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())















