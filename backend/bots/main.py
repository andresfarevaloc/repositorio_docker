from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Conexión a MariaDB
DATABASE_URL = "mysql+pymysql://botuser:botpass123@mariadb:3306/botsdb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Modelo para entrada del usuario
class MensajeEntrada(BaseModel):
    mensaje: str
    usuario: Optional[str] = "usuario"

# Ruta raíz solo para validar conectividad
@app.get("/")
def read_root():
    try:
        db = engine.connect()
        db.close()
        return {"message": "Conexión con MariaDB OK 🚀"}
    except Exception as e:
        return {"error": str(e)}

# Ruta raíz solo para validar Centro de Procesamiento de BOT
@app.get("/cpd")
def read_root():
    try:
        db = engine.connect()
        db.close()
        return {"message": "Conexión con MariaDB OK 🚀"}
    except Exception as e:
        return {"error": str(e)}
