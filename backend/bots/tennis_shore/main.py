from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"bot": "vendiendo tennis está en línea y listo para ayudarte"}