import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = '8741889104:AAGUmCiqlJLt24J9s7H3cmD3Kar3klAnLlw'
ADMIN_ID = 8411839754  # आपका एडमिन आईडी

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('स्वागत है! बॉट चालू है और एडमिन पैनल एक्टिव है।')

# एडमिन ब्रॉडकास्ट कमांड
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("आप एडमिन नहीं हैं!")
        return
    
    msg = " ".join(context.args)
    if not msg:
        await update.message.reply_text("कृपया मैसेज लिखें।")
        return
    
    # यहाँ आप सभी को मैसेज भेजने का कोड जोड़ सकते हैं
    await update.message.reply_text(f"ब्रॉडकास्ट किया गया: {msg}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('broadcast', broadcast))
    
    print("Powerful Bot is running...")
    application.run_polling()
