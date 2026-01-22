from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOOK_PATH = "رفيقك في البرمجة.pdf"  # اسم الملف الذي تريد إرساله

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبًا! أرسل كلمة 'برمجة' للحصول على الكتاب.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "برمجة" in text:
        await update.message.reply_document(open(BOOK_PATH, "rb"))
    else:
        await update.message.reply_text("اكتب كلمة 'برمجة' للحصول على الكتاب!")

if __name__ == "__main__":
    TOKEN = "8302780348:AAHqpxkqZ9mGSxjw2Vd8I4na9jxIS45Bfvo"  # ضع هنا التوكن الذي حصلت عليه من BotFather

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()
