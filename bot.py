import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# आपका टोकन और एडमिन आईडी
TOKEN = '8741889104:AAGUmCiqlJLt24J9s7H3cmD3Kar3klAnLlw'
ADMIN_ID = 8411839754

# लॉगिंग सेट करना ताकि एरर पता चल सके
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('अमरजीत, बॉट रेडी है! APK फाइल भेजें।')

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # एडमिन चेक
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("क्षमा करें, आप एडमिन नहीं हैं!")
        return

    try:
        # फाइल डाउनलोड करना
        document = update.message.document
        file = await document.get_file()
        
        # फोल्डर बनाना
        if not os.path.exists("downloads"):
            os.makedirs("downloads")
            
        file_path = os.path.join("downloads", document.file_name)
        await file.download_to_drive(file_path)
        
        await update.message.reply_text(f"सफलता! फाइल '{document.file_name}' सेव हो गई।")
        
    except Exception as e:
        await update.message.reply_text(f"फाइल प्रोसेसिंग में एरर आया: {str(e)}")
        logging.error(f"Error: {e}")

if __name__ == '__main__':
    # एप्लिकेशन सेटअप
    application = ApplicationBuilder().token(TOKEN).build()
    
    # हैंडलर्स
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    
    print("बॉट सफलतापूर्वक शुरू हो गया है...")
    application.run_polling()
