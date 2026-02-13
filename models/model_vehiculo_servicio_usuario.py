''' Esta clase permite generar el modelo para las ventas y asignaciones'''
from sqlalchemy import Column, Integer, Boolean, DateTime, Date,Time, ForeignKey
from enum import Enum

from config.db import Base

class Estatus(Enum):
    Programado= "Programado"
    Proceso = "En proceso"
    Realizado= "Realizado"

    ''' Clase para escuchar tabla vehiculos '''
class vehiculoServicio(Base):
    __tablename__="vehiculos_servicios_usuarios"
    Id= Column(Integer,primary_key=True, index=True)
    auto_Id= Column(Integer,ForeignKey('c_auto.id'))
    cajero_Id= Column(Integer,ForeignKey('c_usuario.Id'))
    operador_Id= Column(Integer, ForeignKey('c_usuario.Id'))
    servicio_id= Column(Integer, ForeignKey('c_servicio.Id'))
    fecha= Column(Date)
    hora=  Column(Time)
    estatus= Column(Enum(Estatus),default=Estatus.Programado)
    estado= Column(Boolean)
    fecha_registro= Column(DateTime)
    fecha_actualizacion=Column(DateTime)






















