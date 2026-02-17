<<<<<<< HEAD
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
=======

from pydantic import BaseModel
from datetime import datetime

class RolBase(BaseModel):

    nombre_rol:str
    estado: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class RolCreate(RolBase):
        '''Clase para crear un Rol basado en la tabla Rols'''
        pass
    class Rolupdate(RolBase):
        '''Clase para actualizar un Rol basado en la tbla rols'''
        pass
    class Rol(RolBase):
        '''Clase para realizar operaciones por ID en tabla Rol'''
        Id:int
        class Config:
            '''Utilizar el orm para ejecutar las funciones'''
            orm_mode= True







>>>>>>> 70958b0133b0bad4d396fc8a3f4a0718d6588c0a
