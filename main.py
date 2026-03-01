from fastapi import FastAPI
from config.db import Base, engine
from routes import (
    auto_routes,
    rol_routes,
    servicio_routes,
    usuario_routes,
    vehiculo_servicio_routes
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AutoLavado API")

app.include_router(usuario_routes.router)  # Login libre

app.include_router(auto_routes.router)
app.include_router(rol_routes.router)
app.include_router(servicio_routes.router)
app.include_router(vehiculo_servicio_routes.router)