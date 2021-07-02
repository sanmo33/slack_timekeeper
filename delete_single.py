import requests
import random
import logging
logging.basicConfig(level=logging.DEBUG)

import os
import sys
from slack import WebClient
from slack.errors import SlackApiError
import configparser

#引数にURLを入れてね。
timestamp = sys.argv[1]

#tsの取得
timestamp = timestamp[-17:].replace('p','')
timestamp = timestamp[:-6] + '.'+ timestamp[-6:]

config_ini  = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

TOKEN = config_ini['login']['token']
CHANNEL = config_ini['login']['channel']

slack_token = TOKEN
client = WebClient(token=slack_token)

try:
  response = client.chat_delete(
    channel=CHANNEL,
    ts = timestamp,
  )
except SlackApiError as e:
  assert e.response["error"]