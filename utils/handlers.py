from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
import bot_functions.basic_functions as basic_fns
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def log_message(update, context):
    user = update.message.from_user
    logger.info(f"Message from {user.username} ({user.id}): {update.message.text}")
    
def set_bot_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("test", basic_fns.test))
    dispatcher.add_handler(MessageHandler(filters.ALL, log_message))
    