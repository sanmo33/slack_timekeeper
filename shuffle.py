import random

def shuffle(a:list,b:list):
    flag = 0
    while True:
        random.shuffle(a)
        random.shuffle(b)
        junban_list = a+["border"]+b
        #下記条件式にスライスの中に人の名前があるように指定する。
        if '竹内' in junban_list[:7]:
            flag = 1
        
        if flag:
            break

    return junban_list