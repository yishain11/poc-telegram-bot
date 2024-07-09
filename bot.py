import os
from telegram.ext import ApplicationBuilder
import utils.handlers as set_bot

token = os.environ["TELEGRAM_BOT_TOKEN"]
cloud_url = os.environ["POC_TELEGRAM_SERVER"]

def main() -> None:
    app = ApplicationBuilder().token(token).build()
    set_bot.set_bot_handlers(app)
    app.run_polling()
if __name__ == '__main__':
    main()