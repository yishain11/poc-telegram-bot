import requests
import os
import json

server_url = os.environ["POC_TELEGRAM_SERVER"]

async def test(update, context):
    await update.message.reply_text('Hello! I am your bot. testing')

async def ping_server(update, context):
    answer = requests.get(server_url)   
    await update.message.reply_text(json.dumps(answer))
     