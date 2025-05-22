from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"bot": "🤖 AUX_METAL está en línea y listo para ayudarte"}