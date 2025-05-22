# app/main.py
from fastapi import FastAPI
from app.routes import bot_routes

app = FastAPI(title="Bot Operacion MDW")

# Incluir las rutas desde el archivo bot_routes
app.include_router(bot_routes.router)

# Endpoint raiz (opcional para pruebas)
@app.get("/mensaje")
def root():
    return {"message": "Bot Operacion MDW activo y con nuevo mensaje"}