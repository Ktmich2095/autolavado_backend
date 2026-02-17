from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# Inicializar app
app = FastAPI(title="Autolavado API")

# Registrar routers
from config.db import Base, engine
from routes import routes_usuario, routes_rol, routes_servicios, routes_vehiculos, routes_vehiculos_servicios_usuarios


# Crear tablas (solo para desarrollo; en producción usar migraciones)
Base.metadata.create_all(bind=engine)


# Incluir routers definidos en la carpeta routes
app.include_router(routes_usuario.router)
app.include_router(routes_rol.router)
app.include_router(routes_servicios.router)
app.include_router(routes_vehiculos.router)
app.include_router(routes_vehiculos_servicios_usuarios.router)


# Redirigir la raíz "/" a "/docs"
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


# Ruta de saludo simple
@app.get("/saludo", tags=["Saludo"])
def saludo():
    return {"message": "¡Hola, FastAPI!"}
