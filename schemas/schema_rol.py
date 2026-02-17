from pydantic import BaseModel
from datetime import datetime


class RolBase(BaseModel):
    nombre: str
    estatus: bool = True


class RolCreate(BaseModel):
    nombre: str


class RolUpdate(BaseModel):
    nombre: str | None = None
    estatus: bool | None = None


class Rol(RolBase):
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True
