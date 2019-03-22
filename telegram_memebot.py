# 
# Gets a Random Meme when Requesting: /meme
# 
from telegram.ext import Updater, CommandHandler
import requests
import random
import re
import os

start_message = """
Commands available:

/start    ->    Shows this prompt
/meme     ->    Fetches a random meme
"""

def start(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    bot.send_message(chat_id=chat_id, text=start_message)

def get_meme_url():
    urls = requests.get('https://api.imgflip.com/get_memes').json()
    meme_url = urls['data']['memes'][random.randint(1,100)]
    return meme_url

def meme(bot, update):
    url = get_meme_url()
    chat_id = update.message.chat_id
    print(chat_id)
    bot.send_message(chat_id=chat_id, text=url['name'])
    bot.send_photo(chat_id=chat_id, photo=url['url'])

def main():
    updater = Updater(os.environ['TELEGRAM_TOKEN'])
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('meme', meme))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
