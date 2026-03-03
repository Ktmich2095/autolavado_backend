import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from config.db import SessionLocal
import models.user as model_user
import models.rol as model_rol
from config.security import create_access_token
from datetime import timedelta
import uuid
from passlib.context import CryptContext

client = TestClient(app)

@pytest.fixture(scope="module")
def get_auth_token():
    db = SessionLocal()

    # Crear un rol de prueba si no existe
    rol_test = db.query(model_rol.Rol).filter(model_rol.Rol.nombre == "TEST_ROLE").first()
    if not rol_test:
        rol_test = model_rol.Rol(nombre="TEST_ROLE", estado=True)
        db.add(rol_test)
        db.commit()
        db.refresh(rol_test)

    # Asegurarnos de borrar el usuario test si existía
    db_usuario = db.query(model_user.Usuario).filter(model_user.Usuario.correo_electronico == "admin@test.com").first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()

    # Crear usuario de prueba
    pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
    hashed_password = pwd_context.hash("password_segura")

    # Aquí 'rol_Id' es la columna que relaciona con la tabla 'c_rol'
    nuevo_usuario = model_user.Usuario(
        rol_Id=rol_test.Id,  # Asegúrate de usar 'rol_Id' (no 'rol_id')
        nombre="Test",
        apellidoPaterno="User",
        apellidoMaterno="Admin",
        direccion="Test Dir",
        correo_electronico="admin@test.com",
        numero_telefono="0000000000",
        estado=True,
        password=hashed_password
    )
    db.add(nuevo_usuario)
    db.commit()

    # Iniciar sesión
    response = client.post("/login", data={
        "username": "admin@test.com",
        "password": "password_segura"
    })
    token = response.json().get("access_token")

    yield {"Authorization": f"Bearer {token}"}

    # Limpieza
    db.delete(nuevo_usuario)
    db.commit()

    usuarios_con_rol = db.query(model_user.Usuario).filter(model_user.Usuario.rol_Id == rol_test.Id).count()
    if usuarios_con_rol == 0:
        db.delete(rol_test)
        db.commit()

    db.close()


def test_crear_rol_exitoso(get_auth_token):
    headers = get_auth_token
    rol_nombre = f"Rol_{uuid.uuid4().hex[:8]}"  # Usamos más caracteres para evitar colisiones

    payload = {
        "nombre": rol_nombre,  # Cambié NombreRol por nombre
        "estado": True,
        "fecha_registro": "2024-01-01T00:00:00",
        "fecha_actualizacion": "2024-01-01T00:00:00"
    }
    response = client.post("/roles/", json=payload, headers=headers)
    assert response.status_code == 200

    data = response.json()
    assert data["nombre"] == payload["nombre"]
    assert data["estado"] == True
    assert "Id" in data


def test_crear_rol_datos_invalidos(get_auth_token):
    headers = get_auth_token

    payload_invalido = {"rol_id": "no-es-un-numero", "nombre": "Error"}
    response = client.post("/roles/", json=payload_invalido, headers=headers)
    assert response.status_code == 422


def test_crear_rol_faltando_nombre(get_auth_token):
    headers = get_auth_token

    # Enviar un payload sin el campo 'nombre'
    payload_invalido = {"estado": True, "fecha_registro": "2024-01-01T00:00:00", "fecha_actualizacion": "2024-01-01T00:00:00"}
    response = client.post("/roles/", json=payload_invalido, headers=headers)

    # Verificar que el código de estado sea 422 (error de validación)
    assert response.status_code == 422
    assert "detail" in response.json()


def test_crear_rol_estado_invalido(get_auth_token):
    headers = get_auth_token

    # Enviar un payload con un estado inválido (por ejemplo, como string)
    payload_invalido = {"nombre": "Rol Invalido", "estado": "no_booleano", "fecha_registro": "2024-01-01T00:00:00", "fecha_actualizacion": "2024-01-01T00:00:00"}
    response = client.post("/roles/", json=payload_invalido, headers=headers)

    # Verificar que el código de estado sea 422 (error de validación)
    assert response.status_code == 422
    assert "detail" in response.json()