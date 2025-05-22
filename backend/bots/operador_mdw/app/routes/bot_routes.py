from fastapi import APIRouter, Form, Request
from fastapi.responses import PlainTextResponse
from app.database import SessionLocal
from app.models import BotMessages
from datetime import datetime
from app.utils.pdf_generator import generar_pdf_estado, registrar_envio_documento
from app.utils.ver_tablas import obtener_tablas_contenido
import logging

# Configuración de logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

router = APIRouter()

PLATAFORMAS = ["UPF", "WebLogic", "Portal", "Fuse"]

@router.post("/mensaje", response_class=PlainTextResponse)
def manejar_mensaje(From: str = Form(...), Body: str = Form(...)):
    try:
        db = SessionLocal()
        usuario_id = 1  # temporal
        texto = Body.strip().lower()

        logger.debug(f"Mensaje recibido de {From}: {texto}")

        db.add(BotMessages(
            bot_id=1, usuario_id=usuario_id, mensaje=texto,
            tipo="entrada", timestamp=datetime.utcnow(), canal="whatsapp"
        ))
        db.commit()

        # Lógica del bot
        if texto in ["hola", "buenas", "saludos"]:
            respuesta = (
                "Hola, soy el asistente de Andrés Felipe. 🤖\n"
                "¿En qué plataforma necesitas ayuda hoy?\n"
                "1. UPF\n2. WebLogic\n3. Portal\n4. Fuse\n"
                "5. Futuras Respuestas"
            )
        elif any(p.lower() in texto for p in PLATAFORMAS):
            plataforma = next(p for p in PLATAFORMAS if p.lower() in texto)
            generar_pdf_estado(plataforma)
            registrar_envio_documento(bot_id=1)
            respuesta = f"He generado un informe de estado para {plataforma}. ¡Todo está óptimo! 🚀"
        elif "tablas" in texto or "estado interno" in texto:
            contenido = obtener_tablas_contenido()
            respuesta = "Aquí tienes el estado de las tablas del bot:\n\n" + contenido
        elif "como funciona" in texto:
            respuesta = "Claro, puedo explicarte cómo funciona esa plataforma si me lo pides. Estoy disponible las próximas 24 horas."
        elif texto:
            respuesta = (
                "Gracias por tu mensaje. ¿Podrías especificar si necesitas ayuda con UPF, WebLogic, Portal o Fuse?\n"
                "Estoy para ayudarte a resolver cualquier inconveniente en esas plataformas."
            )
        else:
            respuesta = (
                "Ese tema parece fuera de las plataformas que administro.\n"
                "He notificado a Andrés para que te contacte 📢"
            )

        db.add(BotMessages(
            bot_id=1, usuario_id=usuario_id, mensaje=respuesta,
            tipo="salida", timestamp=datetime.utcnow(), canal="whatsapp"
        ))
        db.commit()

        logger.debug(f"Respuesta enviada a {From}: {respuesta}")
        return respuesta

    except Exception as e:
        logger.exception("Error al manejar el mensaje")
        return PlainTextResponse(content="Ha ocurrido un error interno en el bot.", status_code=500)

    finally:
        db.close()
