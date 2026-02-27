from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# Inicializar app
app = FastAPI(title="Autolavado API")

# Importar engine y Base
from config.db import Base, engine

# 🔥 IMPORTAR TODOS LOS MODELOS (IMPORTANTE)
from models import model_usuario
from models import model_rol
from models import model_servicio
from models import model_vehiculo
from models import model_usuario_vehiculo_servicio

# Crear tablas (solo desarrollo)
Base.metadata.create_all(bind=engine)

# Importar routers DESPUÉS
from routes import (
    routes_usuario,
    routes_rol,
    routes_servicio,
    routes_vehiculo,
    routes_usuario_vehiculo_servicio
)

# Incluir routers
app.include_router(routes_usuario.usuario)
app.include_router(routes_rol.rol)
app.include_router(routes_servicio.servicio)
app.include_router(routes_vehiculo.vehiculo)
app.include_router(routes_usuario_vehiculo_servicio.usuario_vehiculo_servicio)

# Redirigir raíz
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")