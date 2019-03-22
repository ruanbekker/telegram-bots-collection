# https://github.com/pyshivam/echoBot

from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, CommandHandler
from telegram.ext.filters import Filters
import requests
import logging
import time
import re
import random
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

words = ['sustainable', 'super']
chat_id_of_channel = os.environ['TELEGRAM_GROUPID']
TOKEN = os.environ['TELEGRAM_TOKEN']

start_message = """
Welcome :-D

/start   ->   Shows this message
/help    ->   Shows something else
filters  ->   When any of the words defined in the words list are entered,
              user will be notified that the words are not allowed.
"""

def tokenizer(input_string):
    response = re.sub('[^A-Za-z0-9]+', ' ', input_string).split()
    return response

def start(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=start_message)

def help(bot, update):
    url = 'https://sayingimages.com/wp-content/uploads/welcome-to-the-danger-zone-meme.jpg'
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    bot.send_message(chat_id=chat_id, text=start_message)

def channel_message(bot, update):
    msg = update.effective_message
    print("Message received from channel: %s" % str(msg['text']))

def reply_msg(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    tokenized = tokenizer(text)
    for each_word in tokenized:
        if each_word in words:
            bot.send_message(chat_id=chat_id, text="Yo {}! {} is not accepted here".format(update.message.chat.first_name, each_word))
    
    print({"date": str(update.message.date), "message_id": update.message.message_id, "chat_id": str(chat_id), "username": update.message.chat.username, "firstname": update.message.chat.first_name, "text": update.message.text})
    
def main():
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("meme", meme))
    updater.dispatcher.add_handler(CommandHandler("help", help))
    updater.dispatcher.add_handler(MessageHandler(Filters.chat(chat_id=chat_id_of_channel), channel_message))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, reply_msg))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
