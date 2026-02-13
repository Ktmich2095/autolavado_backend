from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime


class UsuarioBase(BaseModel):
    rol_Id: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    direccion: str
    correo_electronico: str
    numero_telefono: str
    contrasena :str
    estado: bool
    fecha_registro:DateTime 
    fecha_actualizacion:DateTime

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioUpdate(BaseModel):
    nombre: Optional[str]
    direccion: Optional[str]
    numero_telefono: Optional[str]
    estatus: Optional[bool]

class UsuarioResponse(UsuarioBase):
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True
