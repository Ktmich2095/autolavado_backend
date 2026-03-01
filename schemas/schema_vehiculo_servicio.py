from pydantic import BaseModel
from datetime import datetime, date, time
from enum import Enum


class EstatusSchema(str, Enum):
    Programado = "Programado"
    Proceso = "Proceso"
    Realizado = "Realizado"
    Cancelada = "Cancelada"


class VehiculoServicioBase(BaseModel):
    auto_Id: int
    cajero_Id: int
    operador_Id: int
    servicio_id: int
    fecha: date
    hora: time
    estatus: EstatusSchema
    estado: bool


class VehiculoServicioCreate(VehiculoServicioBase):
    pass


class VehiculoServicioUpdate(BaseModel):
    auto_Id: int | None = None
    cajero_Id: int | None = None
    operador_Id: int | None = None
    servicio_id: int | None = None
    fecha: date | None = None
    hora: time | None = None
    estatus: EstatusSchema | None = None
    estado: bool | None = None


class VehiculoServicioResponse(VehiculoServicioBase):
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    model_config = {
        "from_attributes": True
    }