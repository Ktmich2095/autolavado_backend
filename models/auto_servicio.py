from sqlalchemy import Column, Integer, ForeignKey, DateTime, Time, Boolean, DECIMAL
from sqlalchemy.orm import relationship
from config.db import Base

class AutoServicio(Base):
    __tablename__ = "r_auto_servicio"

    as_id = Column(Integer, primary_key=True, index=True)
    au_id = Column(Integer, ForeignKey("c_auto.au_id"))
    se_id = Column(Integer, ForeignKey("c_servicio.se_id"))
    us_id = Column(Integer, ForeignKey("c_usuario.us_id"))

    as_fecha = Column(DateTime)
    as_hora = Column(Time)
    as_pagado = Column(Boolean)
    as_aprobado = Column(Boolean)
    as_monto = Column(DECIMAL(10,2))

    auto = relationship("Auto", back_populates="servicios")
    servicio = relationship("Servicio", back_populates="autos")
