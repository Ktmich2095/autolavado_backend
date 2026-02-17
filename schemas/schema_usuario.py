<<<<<<< HEAD
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UsuarioBase(BaseModel):
    rol_id: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str | None = None
    direccion: str | None = None
    correo_electronico: EmailStr
    numero_telefono: str | None = None
    estatus: bool = True


class UsuarioCreate(BaseModel):
    rol_id: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str | None = None
    direccion: str | None = None
    correo_electronico: EmailStr
    numero_telefono: str | None = None
    contrasena: str


class UsuarioUpdate(BaseModel):
    rol_id: int | None = None
    nombre: str | None = None
    primer_apellido: str | None = None
    segundo_apellido: str | None = None
    direccion: str | None = None
    correo_electronico: EmailStr | None = None
    numero_telefono: str | None = None
    estatus: bool | None = None
    contrasena: str | None = None


class Usuario(UsuarioBase):
    id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        from pydantic import BaseModel, EmailStr
        from datetime import datetime


        class UsuarioBase(BaseModel):
            rol_id: int
            nombre: str
            primer_apellido: str
            segundo_apellido: str | None = None
            direccion: str | None = None
            correo_electronico: EmailStr
            numero_telefono: str | None = None
            estatus: bool = True


        class UsuarioCreate(BaseModel):
            rol_id: int
            nombre: str
            primer_apellido: str
            segundo_apellido: str | None = None
            direccion: str | None = None
            correo_electronico: EmailStr
            numero_telefono: str | None = None
            contrasena: str


        class UsuarioUpdate(BaseModel):
            rol_id: int | None = None
            nombre: str | None = None
            primer_apellido: str | None = None
            segundo_apellido: str | None = None
            direccion: str | None = None
            correo_electronico: EmailStr | None = None
            numero_telefono: str | None = None
            estatus: bool | None = None
            contrasena: str | None = None


        class Usuario(UsuarioBase):
            id: int
            fecha_registro: datetime
            fecha_actualizacion: datetime

            class Config:
                orm_mode = True
=======
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
>>>>>>> 70958b0133b0bad4d396fc8a3f4a0718d6588c0a
