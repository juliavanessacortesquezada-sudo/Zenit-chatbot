import os
import threading
from dotenv import load_dotenv
from unidecode import unidecode
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 1. CARGAR CONFIGURACIÓN
load_dotenv()
TOKEN = os.getenv("TOKEN")

# 2. CONFIGURACIÓN DE FLASK
web_app = Flask(__name__)

@web_app.route('/')
def health_check():
    return "Zeenit está vivo 🧠✨", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host='0.0.0.0', port=port)

# 3. LÓGICA DEL BOT
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola 👋 Soy ZeenitBot 🧠✨. ¿En qué puedo ayudarte hoy?")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = unidecode(update.message.text.lower())
    palabras = texto.split()

    if any(p in ["cansada", "cansado", "cansancio", "sueño"] for p in palabras):
        res = "Zeenit detecta fatiga 😴. Toma un descanso de 15 min lejos de pantallas."
    elif any(p in ["estres", "ansiedad", "presion"] for p in palabras):
        res = "Zeenit detecta estrés 🧠💥. Prueba respirar profundo: inhala en 4 seg, exhala en 8."
    elif any(p in ["organizacion", "tiempo", "tareas"] for p in palabras):
        res = "La organización reduce la carga mental 📅. ¡Prueba la técnica Pomodoro!"
    else:
        res = "Aún estoy aprendiendo. Pregúntame sobre estrés, cansancio u organización."
    
    await update.message.reply_text(res)

# 4. EJECUCIÓN
if __name__ == "__main__":
    # Verificación de seguridad para el Token
    if not TOKEN:
        print("❌ ERROR: No se encontró el TOKEN. Revisa tu archivo .env")
    else:
        # Hilo para Flask
        threading.Thread(target=run_flask, daemon=True).start()
        
        print("Zeenit arrancando en modo Web Service Gratis...")
        
        # Construcción del Bot
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
        
        app.run_polling()
