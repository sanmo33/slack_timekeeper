import logging
logging.basicConfig(level=logging.DEBUG)

import time
from slack import WebClient
from slack.errors import SlackApiError
import configparser

config_ini  = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

TOKEN = config_ini['login']['token']
CHANNEL = config_ini['login']['channel']

slack_token = TOKEN
client = WebClient(token=slack_token)


def delete(lis:list):
  for timestamp in lis:
    try:
      response = client.chat_delete(
        channel=CHANNEL,
        ts = timestamp,
      )
    except SlackApiError as e:
      assert e.response["error"]
    
    time.sleep(1)