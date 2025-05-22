from app.database import engine
from app import models

print("Creando las tablas...")
models.Base.metadata.create_all(bind=engine)
print("Tablas creadas con éxito.")
