from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"bot": "arreglando ando está en línea y listo para ayudarte"}
    mensaje_usuario = entrada.mensaje.lower()

    if mensaje_usuario in ["hola", "buenos días", "buenas", "menu", "ayuda"]:
        return {
            "respuesta": (
                f"👋 Hola, soy el asistente virtual de Andrés Felipe, "
                f"ingeniero DevOps. ¿Sobre cuál de estas plataformas necesitas ayuda?\n\n"
                "1️⃣ UPF\n"
                "2️⃣ WebLogic\n"
                "3️⃣ Portal\n"
                "4️⃣ Fuse\n\n"
                "Responde con el número o nombre de la plataforma."
            )
        }

    elif "upf" in mensaje_usuario or "1" in mensaje_usuario:
        return {
            "respuesta": "🔍 UPF: plataforma de procesos para facturación. ¿Deseas ver logs o estado?"
        }

    elif "weblogic" in mensaje_usuario or "2" in mensaje_usuario:
        return {
            "respuesta": "🛠️ WebLogic: ¿Quieres ver estado, reiniciar servicios o consultar logs?"
        }

    elif "portal" in mensaje_usuario or "3" in mensaje_usuario:
        return {
            "respuesta": "🌐 Portal: acceso de clientes. Puedes consultar métricas y actividad."
        }

    elif "fuse" in mensaje_usuario or "4" in mensaje_usuario:
        return {
            "respuesta": "🔄 Fuse: integración de flujos. ¿Quieres listar errores recientes?"
        }

    else:
        return {
            "respuesta": (
                "🤖 Lo siento, no entendí tu mensaje. "
                "Escribe 'menu' para ver las opciones disponibles."
            )
        }