from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AutoBase(BaseModel):
    usuario_Id: int
    marca: str
    modelo: str
    placa: str
    serie: str
    color: str
    tipo: str
    anio: int
    estatus: bool
    fecha_registro:datetime
    fecha_actualizacion:datetime

class AutoCreate(AutoBase):
    pass

class AutoResponse(AutoBase):
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True
