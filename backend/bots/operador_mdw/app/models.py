# app/models.py
from sqlalchemy import Column, Integer, String, DateTime, Text, Enum, DECIMAL, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum
from datetime import datetime

Base = declarative_base()

class BotTable(Base):
    __tablename__ = "bot_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_bot = Column(String(50), nullable=False)
    owner_bot = Column(String(50), nullable=False)
    descripcion = Column(Text)
    estado = Column(Enum("activo", "inactivo"), default="activo")
    creado_en = Column(DateTime, default=datetime.utcnow)

class BotUsuario(Base):
    __tablename__ = "bot_usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column(String(100), nullable=False)
    tipo_usuario = Column(Enum("owner", "arrendatario", "publico"), nullable=False)
    email = Column(String(100), nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)

class BotMessages(Base):
    __tablename__ = "bot_messages"
    id = Column(Integer, primary_key=True, autoincrement=True)
    bot_id = Column(Integer, ForeignKey("bot_table.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("bot_usuario.id"), nullable=False)
    mensaje = Column(Text, nullable=False)
    tipo = Column(Enum("entrada", "salida"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    canal = Column(String(30), nullable=False)

class BotGastos(Base):
    __tablename__ = "bot_gastos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    bot_id = Column(Integer, ForeignKey("bot_table.id"), nullable=False)
    descripcion = Column(String(255), nullable=False)
    valor = Column(DECIMAL(10, 2), nullable=False)
    fecha_gasto = Column(DateTime, default=datetime.utcnow)

class BotPlanes(Base):
    __tablename__ = "bot_planes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_plan = Column(String(50), nullable=False)
    mensajes_incluidos = Column(Integer, nullable=False)
    docs_incluidos = Column(Integer, nullable=False)
    descripcion = Column(Text)
    precio_mensual = Column(DECIMAL(10, 2), nullable=False)

class BotRent(Base):
    __tablename__ = "bot_rent"
    id = Column(Integer, primary_key=True, autoincrement=True)
    bot_id = Column(Integer, ForeignKey("bot_table.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("bot_usuario.id"), nullable=False)
    plan_id = Column(Integer, ForeignKey("bot_planes.id"), nullable=False)
    inicio_renta = Column(DateTime, nullable=False)
    fin_renta = Column(DateTime, nullable=False)
    estado = Column(Enum("activa", "vencida", "cancelada"), nullable=False)

class BotSayayin(Base):
    __tablename__ = "bot_sayayin"
    id = Column(Integer, primary_key=True, autoincrement=True)
    bot_id = Column(Integer, ForeignKey("bot_table.id"), nullable=False)
    conteo_envios_doc = Column(Integer, default=0)
    timestamp_ultimo_envio = Column(DateTime, default=datetime.utcnow)

class BotWebhooks(Base):
    __tablename__ = "bot_webhooks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    bot_id = Column(Integer, ForeignKey("bot_table.id"), nullable=False)
    usuario_id = Column(Integer, nullable=False)
    tipo_evento = Column(Enum("mensaje", "entrega", "estado"), nullable=False)
    payload_raw = Column(Text)
    fecha_evento = Column(DateTime, default=datetime.utcnow)
    openai_usado = Column(Boolean, default=False)
