import os
import threading
from dotenv import load_dotenv
from unidecode import unidecode
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

#.env
load_dotenv()

# configuracion de flask
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
    # 1. Obtenemos el mensaje y lo pasamos a minúsculas
    texto_original = update.message.text.lower()
    
    # LIMPIEZA
    texto_limpio = unidecode(texto_original)
    
    # 3. CREAMOS UNA LISTA DE PALABRAS (para buscar con más precisión)
    palabras = texto_limpio.split()

    # --- LÓGICA DE RESPUESTA MEJORADA ---
    
    # Buscamos variaciones de cansancio
    if any(palabra in ["cansada", "cansado", "cansancio", "sueño", "fatiga", "dormir"] for palabra in palabras):
        respuesta = (
            "Zeenit detecta fatiga académica 😴\n\n"
            "Consejo experto: Si has estudiado más de 2 horas seguidas, tu cerebro ya no está absorbiendo info. "
            "Toma un descanso de 15 min lejos de las pantallas."
        )

    # Buscamos variaciones de estrés
    elif any(palabra in ["estres", "ansiedad", "ansiosa", "presion", "agobiada", "agobiado"] for palabra in palabras):
        respuesta = (
            "Zeenit detecta niveles altos de cortisol (estrés) 🧠💥\n\n"
            "Prueba la técnica 4-7-8: Inhala 4 segundos, mantén 7, exhala 8. "
            "Esto calma tu sistema nervioso inmediatamente."
        )

    # Buscamos variaciones de organización
    elif any(palabra in ["organizacion", "tiempo", "tareas", "horario", "prioridades"] for palabra in palabras):
        respuesta = (
            "La organización reduce la carga mental 📅\n\n"
            "Tip pro: No anotes 'Estudiar'. Anota 'Leer 5 páginas de Química'. "
            "Las tareas pequeñas son más fáciles de empezar."
        )

    else:
        respuesta = (
            "Aún estoy aprendiendo, pero puedo ayudarte con tu **estrés**, **cansancio** u **organización**. "
            "¿Cómo te sientes hoy?"
        )

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
