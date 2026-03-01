from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional


class UsuarioBase(BaseModel):
    rol_Id: int
    nombre: str
    apellidoPaterno: str
    apellidoMaterno: str
    direccion: str
    correo_electronico: str
    numero_telefono: str
    estado: bool


class UsuarioCreate(UsuarioBase):
    password: str

    # bcrypt solo admite contraseñas de hasta 72 bytes.
    # Este validador evita que se envíe una cadena más larga y provoca 422
    # en lugar de un 500 interno.
    @validator("password")
    def password_max_length(cls, v: str) -> str:
        if len(v.encode("utf-8")) > 72:
            raise ValueError("La contraseña no puede superar 72 bytes")
        return v


class UsuarioUpdate(BaseModel):
    rol_Id: Optional[int] = None
    nombre: Optional[str] = None
    apellidoPaterno: Optional[str] = None
    apellidoMaterno: Optional[str] = None
    direccion: Optional[str] = None
    correo_electronico: Optional[str] = None
    numero_telefono: Optional[str] = None
    estado: Optional[bool] = None


class UsuarioResponse(BaseModel):
    Id: int
    nombre: str
    correo_electronico: str
    fecha_registro: datetime | None = None
    fecha_actualizacion: datetime | None = None

    model_config = {
        "from_attributes": True
    }