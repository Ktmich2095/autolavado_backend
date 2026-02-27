'''Esta clase permite generar el modelo para los vehiculos'''
from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
# pylint: disable=import-error
from config.db import Base
from sqlalchemy.orm import relationship

# pylint: disable=too-few-public-methods
class Vehiculo(Base):
    '''Clase para especificar tabla vehiculos'''
    __tablename__ = "tbb_vehiculos"
    Id = Column(Integer, primary_key=True, index=True)
    usuario_Id = Column(Integer, ForeignKey("tbb_usuarios.Id"))
    marca = Column(String(60))
    modelo = Column(String(10))
    placa = Column(String(10))
    serie = Column(String(60))
    color = Column(String(60))
    tipo = Column(String(50))
    anio = Column(Integer)
    estatus = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)

    usuarios = relationship("Usuario", back_populates="vehiculos")
    usuarios_vehiculos_servicios_V = relationship("UsuarioVehiculoServicio", back_populates="vehiculos")
