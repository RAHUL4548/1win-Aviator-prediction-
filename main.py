import logging
import random
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔐 Telegram Bot Token
BOT_TOKEN = "7148656994:AAGYl60jyvFraTvA6M5qLQHOXsyLR3vssS4"  # ← यहां अपना Bot Token डालें

# 📃 Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 🟢 /start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Welcome to 1win Aviator Predictor Bot!\nType /predict to get prediction.")

# 🎯 Prediction Logic
def get_prediction():
    now = datetime.now()
    second = now.second

    # Time-based logic for prediction multiplier
    if second % 5 == 0:
        return "🟥 x1.8 (Be cautious)"
    elif second % 10 == 0:
        return "🟨 x2.5 (Moderate chance)"
    elif second % 13 == 0:
        return "🟩 x7.2 (High confidence)"
    else:
        return f"🟦 x{round(random.uniform(1.2, 3.0), 2)}"

# 🔵 /predict Command
async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = get_prediction()
    await update.message.reply_text(f"🎯 Prediction: {result}")

# 🚀 Bot Setup
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predict", predict))

    logger.info("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
