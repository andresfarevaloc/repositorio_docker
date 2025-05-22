from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Conexión a MariaDB
DATABASE_URL = "mysql+pymysql://botuser:botpass123@mariadb:3306/botsdb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Modelo para entrada del usuario
class MensajeEntrada(BaseModel):
    mensaje: str
    usuario: Optional[str] = "usuario"

# Ruta raíz solo para validar Centro de Procesamiento de BOT
@app.get("/")
def read_root():
    try:
        db = engine.connect()
        db.close()
        return {"message": "Conexión con MariaDB OK 🚀"}
    except Exception as e:
        return {"error": str(e)}

# Ruta POST para interacción del bot
@app.post("/")
def responder_bot(mensaje_usuario: str) -> str:
    mensaje_usuario = mensaje_usuario.lower()

    if mensaje_usuario in ["hola", "buenos días", "buenas", "menu", "ayuda"]:
        return (
            "👋 Hola, soy el asistente virtual de Andrés Felipe, "
            "ingeniero DevOps. ¿Sobre cuál de estas plataformas necesitas ayuda?\n\n"
            "1️⃣ UPF\n"
            "2️⃣ WebLogic\n"
            "3️⃣ Portal\n"
            "4️⃣ Fuse\n\n"
            "Responde con el número o nombre de la plataforma."
        )

    elif "upf" in mensaje_usuario or "1" in mensaje_usuario:
        return "🔍 UPF: plataforma de procesos para facturación. ¿Deseas ver logs o estado?"

    elif "weblogic" in mensaje_usuario or "2" in mensaje_usuario:
        return "🛠️ WebLogic: ¿Quieres ver estado, reiniciar servicios o consultar logs?"

    elif "portal" in mensaje_usuario or "3" in mensaje_usuario:
        return "🌐 Portal: acceso de clientes. Puedes consultar métricas y actividad."

    elif "fuse" in mensaje_usuario or "4" in mensaje_usuario:
        return "🔄 Fuse: integración de flujos. ¿Quieres listar errores recientes?"

    else:
        return "🤖 Lo siento, no entendí tu mensaje. Escribe 'menu' para ver las opciones disponibles."

# Endpoint para uso desde Postman
@app.post("/")
def procesar_mensaje(entrada: MensajeEntrada):
    return {"respuesta": responder_bot(entrada.mensaje)}

# Endpoint webhook para integrarse con Twilio y WhatsApp
@app.post("/webhook")
async def webhook_twilio(
    Body: str = Form(...),
    From: str = Form(...)
):
    print(f"📨 Mensaje recibido de {From}: {Body}")

    respuesta = responder_bot(Body)

    return PlainTextResponse(
        content=f"<Response><Message>{respuesta}</Message></Response>",
        media_type="application/xml"
    )    