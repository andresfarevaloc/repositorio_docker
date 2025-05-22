from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"bot": "Restaurante del sabor aqui vamos está en línea y listo para ayudarte"}