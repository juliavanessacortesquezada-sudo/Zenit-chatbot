from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8752759358:AAGsh5tbTIL8iQ41QO4L5KnnTAeVBle4mnQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola 👋 Soy ZeenitBot 🧠✨\n"
        "Soy un asistente de hábitos saludables para estudiantes universitarios.\n\n"
        "Puedes preguntarme sobre:\n"
        "- Organización del tiempo\n"
        "- Estrés\n"
        "- Cansancio\n"
        "- Técnicas de estudio"
    )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text.lower()

    if "cansancio" in mensaje or "cansada" in mensaje:
        respuesta = (
            "Parece que podrías estar experimentando fatiga académica 📚😴\n\n"
            "Te recomiendo:\n"
            "- Dormir al menos 7 horas\n"
            "- Aplicar la técnica Pomodoro\n"
            "- Tomar descansos cada 50 minutos"
        )

    elif "estrés" in mensaje or "estres" in mensaje:
        respuesta = (
            "El estrés es común en la universidad 😔\n\n"
            "Te recomiendo:\n"
            "- Respiración profunda 5 minutos\n"
            "- Organizar tus tareas por prioridad\n"
            "- Hacer pausas activas"
        )

    elif "organización" in mensaje or "tiempo" in mensaje:
        respuesta = (
            "La organización es clave 📅\n\n"
            "Prueba:\n"
            "- Lista de tareas diaria\n"
            "- Técnica Pomodoro\n"
            "- Establecer horarios fijos"
        )

    else:
        respuesta = "Lo siento, aún estoy aprendiendo 🤖✨ Intenta preguntarme sobre estrés, cansancio u organización."

    await update.message.reply_text(respuesta)

# ... (tus funciones start y responder se quedan igual)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

if __name__ == "__main__":
    print("Zeenit está encendido...")
    # Esta es la forma correcta y simplificada de ejecutar el bot
    app.run_polling()
