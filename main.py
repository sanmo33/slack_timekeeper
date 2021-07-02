import random
from typing import ChainMap
import logging
logging.basicConfig(level=logging.DEBUG)

import time
import datetime
import configparser

from scrapbox import make_scrapbox
from send_message import send_message
from delete_list import delete
from shuffle import shuffle

config_ini  = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

lis1 = eval(config_ini.get('zemisei_list', 'lis1'))
lis2 = eval(config_ini.get('zemisei_list', 'lis2'))

#ts_list.txtの既存のtimestampを削除
with open('ts_list.txt', mode='w') as f:
    f.write('')

with open('check.txt', mode='r')as f:
    tmp = int(f.read())

    #0のときlis1が最初、1のときlis2が最初
    if tmp == 0:
        junban_list = shuffle(lis1,lis2)
    else:
        junban_list = shuffle(lis2,lis1)
    
    with open('check.txt', mode='w')as g:
        if tmp == 0:
            g.write('1')
        else:
            g.write('0')

junban = ''
ind = 1
scrapbox_junban = ''

for i in range(len(junban_list)):
    if junban_list[i] == "border":
        junban += "=====\n"
    else:
        junban += str(ind)+','+junban_list[i]+'\n'
        ind += 1
    
    if junban_list[i] != "border":
        scrapbox_junban += junban_list[i] +'さん'+'\n\n'

send_message(junban)

#scrapboxのノート作成↓
make_scrapbox(scrapbox_junban)

send_message('3分後に開始します。\n'+junban_list[0]+'さんから始まります:man-tipping-hand:')
time.sleep(180)

ch = '<!channel> '
flag = 0
zenhan_minites = 10
kohan_minites = 30
zenhan_minites_minite = datetime.timedelta(minutes=zenhan_minites)
kohan_minites_minite = datetime.timedelta(minutes=kohan_minites)


otukare_list = [":smile:", ":smiley:",":blush:",":smile_cat:",":hatching_chick:",":cactus:",":tada:",":whale2:",":bulb:",
                ":man-lifting-weights:",":yen:",":scientist:",":eyes:",":100:"]

for i in range(len(junban_list)):
    dt = datetime.datetime.now()
    

    if junban_list[i] == "border":
        send_message(ch+'10分休憩しましょう:pizza:')
        flag = 1
        time.sleep(480)
        send_message(ch+'休憩時間は残り2分です:woman-running::man-running:')
        send_message('次は'+junban_list[i+1]+'さんです。')
        time.sleep(120)
        continue

    if flag == 0:
        after_10 = dt + zenhan_minites_minite
        finish_time = after_10.strftime("%H:%M:%S")
        ratio_8 = int(zenhan_minites * 0.8)
        ratio_2 = int(zenhan_minites * 0.2)
        send_message(ch+junban_list[i]+'さんの番・時間は{}分です。'.format(zenhan_minites))
        send_message('終了目安:'+finish_time)
        time.sleep(ratio_8*60)
        send_message(ch+junban_list[i]+'さん、残り{}分です。'.format(ratio_2))
        time.sleep(ratio_2*60)
    else:
        after_30 = dt + kohan_minites_minite
        finish_time = after_30.strftime("%H:%M:%S")
        ratio_8 = int(kohan_minites * 0.8)
        ratio_2 = int(kohan_minites * 0.2)
        send_message(ch+junban_list[i]+'さんの番・時間は{}分です。'.format(kohan_minites))
        send_message('終了目安:'+finish_time)
        time.sleep(ratio_8*60)
        send_message(ch+junban_list[i]+'さん残り{}分です。'.format(ratio_2))
        time.sleep(ratio_2*60)
    
    send_message(ch+junban_list[i]+'さんお疲れさまでした'+random.choice(otukare_list))

    #次の人の指名処理
    try:
        if junban_list[i+1] == "border":
            pass
        else:
            send_message('次は'+junban_list[i+1]+'さんです。\n一分後に開始します。')
            time.sleep(60)
    except:
        pass


send_message('本日は皆様お疲れ様でした！:clap::clap:')

time.sleep(60)
timestamp_list = []

#ts_listからtimestampを読み込んでtimestamp_listにappend
with open('ts_list.txt', 'r')as f:
    for line in f:
        line = line.strip()
        timestamp_list.append(line)

#lisのtimestampを削除
delete(timestamp_list[1:])

#deleted_tsに削除済みのtsを入れる。
with open('deleted_ts.txt', mode='a')as f:
    f.write('\n'.join(timestamp_list[1:]))