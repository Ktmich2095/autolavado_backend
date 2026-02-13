from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ServicioBase(BaseModel):
    nombre: str
    descripcion: str
    costo: float
    duracion: int
    estado: bool

class ServicioCreate(ServicioBase):
    pass

class ServicioUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]
    costo: Optional[float]
    duracion: Optional[int]
    estado: Optional[bool]

class ServicioResponse(ServicioBase):
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True
