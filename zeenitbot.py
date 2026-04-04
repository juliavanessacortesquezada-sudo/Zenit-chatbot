import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# --- CONFIGURACIÓN DE FLASK PARA ENGAÑAR A RENDER ---
web_app = Flask(__name__)

@web_app.route('/')
def health_check():
    return "Zeenit está vivo 🧠✨", 200

def run_flask():
    # Render asigna un puerto automáticamente en la variable PORT
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host='0.0.0.0', port=port)

# --- CÓDIGO DEL BOT ---
TOKEN = os.getenv("TOKEN") 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola 👋 Soy ZeenitBot 🧠✨...")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text.lower()
    # ... (el resto de tu lógica de respuestas igual)
    respuesta = "Lo siento, aún estoy aprendiendo..." # Ejemplo
    await update.message.reply_text(respuesta)

# --- EJECUCIÓN ---
if __name__ == "__main__":
    # 1. Lanzamos Flask en un hilo separado (background)
    threading.Thread(target=run_flask, daemon=True).start()
    
    # 2. Arrancamos el bot normalmente
    print("Zeenit arrancando en modo Web Service Gratis...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    
    app.run_polling()
