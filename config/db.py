'''Establece la conexión con el servidor de Base de Datos'''
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# read connection string from environment or fallback to a local sqlite file
database_url = os.getenv("SQLALCHEMY_DATABASE_URL")
if not database_url:
    # if the user forgot to create a .env or set the variable, fall back to sqlite
    # and warn so the problem is easier to diagnose
    print("[WARNING] SQLALCHEMY_DATABASE_URL not defined, using sqlite:///./autolavado.db")
    # default to sqlite; avoid introducing incorrect dialect names
    database_url = "sqlite:///./autolavado.db"

# when using SQLite we need a special connect_args
connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}

# attempt to create engine, but if connection fails fall back to sqlite
try:
    engine = create_engine(database_url, connect_args=connect_args)
    # optionally test connection now
    with engine.connect() as conn:
        pass
except Exception as exc:
    print(f"[ERROR] Could not connect to database at '{database_url}': {exc}")
    print("[WARNING] Falling back to sqlite:///./autolavado.db")
    database_url = "sqlite:///./autolavado.db"
    connect_args = {"check_same_thread": False}
    engine = create_engine(database_url, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()