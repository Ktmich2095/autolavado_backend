from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ServicioBase(BaseModel):
    nombre: str
    descripcion: str
    costo: float
    duracion_minutos: int
    estado: bool


class ServicioCreate(ServicioBase):
    pass


class ServicioUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    costo: Optional[float] = None
    duracion_minutos: Optional[int] = None
    estado: Optional[bool] = None


class ServicioResponse(ServicioBase):
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    model_config = {
        "from_attributes": True
    }