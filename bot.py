from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os  # لإحضار متغيرات البيئة

# اسم الملف الذي تريد إرساله
BOOK_PATH = "رفيقك في البرمجة.pdf"

# رسالة الترحيب عند /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبًا! أرسل كلمة 'برمجة' للحصول على الكتاب.")

# التعامل مع أي رسالة نصية
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "برمجة" in text:
        await update.message.reply_document(open(BOOK_PATH, "rb"))
    else:
        await update.message.reply_text("اكتب كلمة 'برمجة' للحصول على الكتاب!")

if __name__ == "__main__":
    # قراءة التوكن من Environment Variable
    TOKEN = os.environ['TOKEN']

    # إنشاء التطبيق
    app = ApplicationBuilder().token(TOKEN).build()

    # إضافة الأوامر والرسائل
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()
