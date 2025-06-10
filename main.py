import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from prediction import get_prediction

# Bot Token
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Start command
async def start(update, context):
    await update.message.reply_text("🚀 Welcome to 1win Aviator Predictor Bot!")

# Predict command
async def predict(update, context):
    result = get_prediction()
    await update.message.reply_text(f"🎯 Prediction: {result}")

# Setup
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predict", predict))

    logger.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
