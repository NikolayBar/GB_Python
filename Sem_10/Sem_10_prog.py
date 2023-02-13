import os
import telebot
from pprint import pprint
os.system('clear')

data = open('TokenText.txt', mode='r', encoding='utf-8')
API_TOKEN = data.read()
data.close

bot = telebot.TeleBot(API_TOKEN, parse_mode=None)

def send_result(id,quest,answ):
    bot.send_message(id,f'{quest}\n{answ}')


data = open('log.txt', 'r', encoding='utf-8')
text = data.readlines()
data.close


for el in text:
    el= el[:-1]
    cur_quest = el.split(':')
    id = cur_quest[0]
    quest = cur_quest[1]
    answ = input(f'Вопрос: {quest}\nОтвет ->:')
    if answ !='':
        send_result(id,quest,answ)

pprint(text)
