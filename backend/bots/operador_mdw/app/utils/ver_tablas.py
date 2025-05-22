from app.database import SessionLocal
from sqlalchemy import text
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
import os

# Conexión a la base de datos
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://botuser:botpass123@mariadb:3306/botsdb"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

def obtener_tablas_contenido():
    db = SessionLocal()
    tablas = [
        "bot_gastos", "bot_messages", "bot_planes", "bot_rent",
        "bot_sayayin", "bot_table", "bot_usuario", "bot_webhooks"
    ]
    salida = ""

    for tabla in tablas:
        salida += f"\n📋 Contenido de la tabla: {tabla}\n"
        try:
            resultado = db.execute(text(f"SELECT * FROM {tabla}")).fetchall()
            if resultado:
                for fila in resultado:
                    salida += f"  {dict(fila._mapping)}\n"
            else:
                salida += "  (vacía)\n"
        except Exception as e:
            salida += f"  ❌ Error leyendo tabla '{tabla}': {str(e)}\n"

    db.close()
    return salida