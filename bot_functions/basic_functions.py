import requests
import os
import json
from datetime import datetime

server_url = os.environ["POC_TELEGRAM_SERVER"]

async def test(update, context):
    current_date = datetime.now().strftime("%d-%m-%Y")
    response = requests.get('https://httpbin.org/ip')
    ip_info = response.json()['origin']
    await update.message.reply_text(f'Hello! I am your bot. testing in ${current_date}@{ip_info}')

async def ping_server(update, context):
    answer = requests.get(server_url)   
    await update.message.reply_text(json.dumps(answer))
     