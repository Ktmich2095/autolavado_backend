from pydantic import BaseModel
from datetime import datetime


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


class AutoCreate(AutoBase):
    pass


class AutoUpdate(BaseModel):
    usuario_Id: int | None = None
    marca: str | None = None
    modelo: str | None = None
    placa: str | None = None
    serie: str | None = None
    color: str | None = None
    tipo: str | None = None
    anio: int | None = None
    estatus: bool | None = None


class AutoResponse(AutoBase):
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    model_config = {
        "from_attributes": True
    }