from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
from sqlalchemy.sql import func
class Rol(Base):
    __tablename__ = "c_rol"

    Id = Column(Integer, primary_key=True, index=True)  # === CORREGIDO ===
    nombre = Column(String(45), nullable=False)
    estado = Column(Boolean)

    usuarios = relationship("Usuario", back_populates="rol")  # === NUEVO ===

    fecha_registro = Column(DateTime, default=func.now())
    fecha_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())