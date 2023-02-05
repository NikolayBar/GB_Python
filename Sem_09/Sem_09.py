import telebot
from random import randint as ri
import requests

data = open('TokenText.txt', mode='r', encoding='utf-8')
API_TOKEN = data.read()
data.close

bot = telebot.TeleBot(API_TOKEN, parse_mode=None)

# Handles all text messages that contains the commands '/start' or '/help'
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f"Привет, {message.from_user.first_name}")

# Simple calculator
@bot.message_handler(commands=['calc'])
def send_calc(message):
    msg = bot.reply_to(message, f"Что подсчитать?")
    bot.register_next_step_handler(msg, process_calc)

def process_calc(message):
    try:
        num_str = message.text
        tru_sym =('+','-','/','*','^','%','(',')',' ')
        test = num_str.replace('**','^')
        for x in tru_sym:
            test = test.replace(x,'')
        if test.isdigit():
            answ = f' = {eval(num_str)}'
        else: 
            answ = f'{num_str} < oops, пока только арифметика, не алгебра!'
        bot.reply_to(message, answ)
    except Exception as e:
        bot.reply_to(message, 'oooops')
    
# END Simple calculator


@bot.message_handler(content_types=['text'])
def echo_all(message):
    if message.text == 'погода':
        data = requests.get('https://wttr.in/?format=4')
        bot.reply_to(message,data.text)

    else:
        print(f' {message.from_user.first_name} {message.from_user.last_name}: {message.text}')

bot.infinity_polling()


