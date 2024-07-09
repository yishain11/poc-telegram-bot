import os
from telegram.ext import Updater

import utils.handlers as set_bot

token = os.environ["TELEGRAM_BOT_TOKEN"]
cloud_url = os.environ["POC_TELEGRAM_SERVER"]

def main() -> None:
    updater = Updater(token)
    dispatcher = updater.dispatcher
    set_bot.set_bot_handlers(dispatcher)
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
