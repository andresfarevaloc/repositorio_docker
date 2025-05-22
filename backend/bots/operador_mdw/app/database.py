# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexión para contenedor MariaDB
DATABASE_URL = "mysql+pymysql://botuser:botpass123@mariadb:3306/botsdb"

# Crear motor de conexión
engine = create_engine(DATABASE_URL)

# Configurar sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos SQLAlchemy
Base = declarative_base()