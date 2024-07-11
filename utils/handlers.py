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
    
def set_bot_handlers(app):
    test_handler = CommandHandler('test',basic_fns.test)
    test_handler = CommandHandler('server',basic_fns.ping_server)
    app.add_handler(test_handler)