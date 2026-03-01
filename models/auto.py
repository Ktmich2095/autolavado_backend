from sqlalchemy import Column, Integer, String,Boolean,Float,DateTime,ForeignKey
# from sqlalchemy.orm import relationship
from config.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
class Auto(Base):
    __tablename__ = "c_auto"

    Id = Column(Integer, primary_key=True, index=True)
    usuario_Id = Column(Integer, ForeignKey("c_usuario.Id"))

    marca = Column(String(80))
    modelo = Column(String(45))
    placa = Column(String(45))
    serie = Column(String(45))
    color = Column(String(60))
    tipo = Column(String(45))
    anio = Column(Integer)
    estatus = Column(Boolean)

    usuario = relationship("Usuario", back_populates="autos")  # === NUEVO ===
    servicios = relationship("VehiculoServicio", backref="auto")

    fecha_registro = Column(DateTime, default=func.now())
    fecha_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())