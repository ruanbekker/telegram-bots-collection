# -*- coding: utf-8 -*-
# source:
# https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = ""

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

start_message = """

Welcome :-D

/start   ->   Shows this message
"""

def start(update, context):
    update.message.reply_text(start_message)

def echo(update, context):
    update.message.reply_text(update.message.text)
    logger.info("@{} says: {}".format(update.message.chat.username, update.message.text))

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
