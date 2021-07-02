import random
import logging
logging.basicConfig(level=logging.DEBUG)

from slack import WebClient
from slack.errors import SlackApiError
import configparser


config_ini  = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

TOKEN = config_ini['login']['token']
CHANNEL = config_ini['login']['channel']

slack_token = TOKEN
client = WebClient(token=slack_token)

icon_list =["https://umamusume.jp/app/wp-content/uploads/2021/01/479aa3863ac6d45e0a81b9cf21b5bf8d.png",
            "https://umamusume.jp/app/wp-content/uploads/2021/01/c8d87c6473d75c753682e1bbf4c19b36.png",
            "https://umamusume.jp/app/wp-content/uploads/2021/01/97d92bf10c18d56e86cc1ffea3c58c80.png",
            "https://umamusume.jp/app/wp-content/uploads/2021/01/7c08cc40e8f5c81d4fb6de2acfc3fa66.png",
            "https://umamusume.jp/app/wp-content/uploads/2021/01/8f2b00b0a6cac5464a3d62e583f7c13d.png",
            "https://umamusume.jp/app/wp-content/uploads/2021/01/6c598463ee5c1566023fbf03c4e579cb.png",
            ]
def send_message(honbun:str):
    try:
        response = client.chat_postMessage(
            channel=CHANNEL,
            text=honbun,
            icon_url = random.choice(icon_list),
        )
        ts = response.get('ts')
        with open('ts_list.txt', mode='a')as f:
            f.write(ts)
            f.write('\n')

    except SlackApiError as e:
        assert e.response["error"]

