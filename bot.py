from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# رابط الإحالة الخاص بك من Admitad
AFFILIATE_TEMPLATE = "https://rzekl.com/g/1e8d1144940bca195b9a16525dc3e8/?ulp="

# استجابة عند بدء المحادثة
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبًا! أرسل لي رابط منتج من AliExpress وسأعطيك رابط التخفيض.")

# معالجة الروابط
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "aliexpress.com" in text:
        from urllib.parse import quote_plus
        encoded_url = quote_plus(text)
        affiliate_link = AFFILIATE_TEMPLATE + encoded_url
        await update.message.reply_text(f"هذا هو رابطك مع التخفيض:\n{affiliate_link}")
    else:
        await update.message.reply_text("من فضلك أرسل رابط منتج من AliExpress فقط.")

if __name__ == '__main__':
    import os
    # رمز البوت الخاص بك
    BOT_TOKEN = "7827807490:AAGIpzprahe8nh6BqorXRSfsZcfjm818c3I"
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("البوت يعمل...")
    app.run_polling()