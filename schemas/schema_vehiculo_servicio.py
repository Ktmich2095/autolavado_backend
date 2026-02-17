from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional

from enum import Enum

class EstatusSchema(str, Enum):
    Programado = "Programado"
    Proceso = "En proceso"
    Realizado = "Realizado"

class VehiculoServicioBase(BaseModel):
    auto_Id: int
    cajero_Id: int
    operador_Id: int
    servicio_id: int
    fecha: date
    hora: time
    estatus
    
    
    
    atus: EstatusSchema
    estado: bool

class VehiculoServicioCreate(VehiculoServicioBase):
    pass

class VehiculoServicioResponse(VehiculoServicioBase):
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True

