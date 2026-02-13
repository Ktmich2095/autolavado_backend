from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.db import Base

class Cliente(Base):
    __tablename__ = "c_cliente"

    cl_id = Column(Integer, primary_key=True, index=True)
    cl_nombre = Column(String(60))
    cl_apellidoPaterno = Column(String(60))
    cl_apellidoMaterno = Column(String(60))
    cl_direccion = Column(String(255))
    cl_email = Column(String(55))
    cl_telefono = Column(String(15))
    cl_password = Column(String(750))

    autos = relationship("Auto", back_populates="cliente")
