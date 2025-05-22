FROM python:3.11-slim

WORKDIR /app

# El archivo ahora debe estar dentro del contexto (cada bot)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del bot (main.py, etc.)
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]