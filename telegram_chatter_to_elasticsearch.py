#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ast
import os
import json
import time
import logging
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers

ES_ENDPOINT = os.environ['ES_ENDPOINT']
ES_USER = os.environ['ES_USER']
ES_PASSWORD = os.environ['ES_PASSWORD']
ES_INDEX = os.environ['ES_INDEX']

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

es = Elasticsearch(
    hosts = [{'host': ES_ENDPOINT, 'port': 443}],
    http_auth=(ES_USER, ES_PASSWORD), use_ssl=True, verify_certs=True,
    connection_class=RequestsHttpConnection
)

start_message = """

Welcome :-D

/start   ->   Shows this message
"""

def convert_time(epoch):
    datestamp = time.strftime('%Y-%m-%d', time.localtime(epoch))
    return datestamp

def start(update, context):
    update.message.reply_text(start_message)

def search(update, context):
    print("BotId: {}, ArgsPassed: {}".format(context.bot.id, context.args))
    term = " ".join(context.args)
    response = es.search(index=ES_INDEX, doc_type="_doc", body={"query": {"match": {"text": term}}})
    docs_found = response['hits']['total']
    if docs_found > 1:
        update.message.reply_text(parse_mode=ParseMode.MARKDOWN, text="Search matched *{}* documents".format(docs_found))
    else:
        update.message.reply_text(parse_mode=ParseMode.MARKDOWN, text="Search matched *{}* document".format(docs_found))
    for doc in response['hits']['hits']:
        search_result = "Date: {}\nUsername: {}\nMessage: {}".format(convert_time(doc['_source']['date']), doc['_source']['chat']['username'], doc['_source']['text'])
        update.message.reply_text(search_result)

def ship_to_elasticsearch(update, context):
    payload = ast.literal_eval(str(update.message))
    print("payload: {}".format(payload))
    response = es.index(index=ES_INDEX, doc_type='_doc', body=payload)
    es_index_id = response['_id']
    update.message.reply_text("Message {}, shipped to elasticsearch index id: {}".format(update.message.message_id, es_index_id))
    logger.info("@{} says: {}".format(update.message.chat.username, update.message.text))

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater("945686971:x", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("search", search))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, ship_to_elasticsearch))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
