from pydantic import BaseModel
from datetime import datetime


class RolBase(BaseModel):
    nombre: str
    estado: bool


class RolCreate(RolBase):
    pass


class RolUpdate(BaseModel):
    nombre: str | None = None
    estado: bool | None = None


class RolResponse(RolBase):
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    model_config = {
        "from_attributes": True
    }