import telebot
from random import randint as ri
import requests

data = open('TokenText.txt', mode='r', encoding='utf-8')
API_TOKEN = data.read()
data.close
game = False
hiden_num = None
step_game = 0

bot = telebot.TeleBot(API_TOKEN, parse_mode=None)

# Handles all text messages that contains the commands '/start' or '/help'
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f"Привет, {message.from_user.first_name}")

@bot.message_handler(commands=['calc'])
def send_calc(message):
    msg = bot.reply_to(message, f"Что считаем?")
    bot.register_next_step_handler(msg, process_calc)


# калькулятор
def process_calc(message):
    try:
        num_str = message.text
        tru_sym =('+','-','/','*','^','%','(',')',' ')
        test = num_str.replace('**','^')
        for x in tru_sym:
            test = test.replace(x,'')
        if test.isdigit():
            answ = f'= {eval(num_str)}'
        else: 
            answ = f'{num_str} < oops, пока только арифметика, не алгебра!'
        bot.reply_to(message, answ)
    except Exception as e:
        bot.reply_to(message, 'oooops')


# обработка текстовых сообщений
@bot.message_handler(content_types=['text'])
def echo_all(message):
    global game
    global hiden_num
    msg = message.text
    if  msg == 'погода':
        print(msg)
        data = requests.get('https://wttr.in/?format=4')
        bot.reply_to(message,data.text)
        pass
    elif msg in ['играть', 'игра','game']:
        if game == False:
            game = True 
            hiden_num = ri(1,1000)
            msg = bot.reply_to(message, f"Загадал число от 1 до 1000")
            bot.register_next_step_handler(msg, process_game)
        else:
            msg = bot.reply_to(message, f"Игра уже запущена")
            bot.register_next_step_handler(msg, process_game)
        pass
    elif msg in ['calc', 'считать', 'калькулятор']:
        msg = bot.reply_to(message, f"Что считаем?")
        bot.register_next_step_handler(msg, process_calc)
    else:
        print(f'last row {message.from_user.first_name} {message.from_user.last_name}: {message.text}')


# логика игры угадай число
def process_game(message):
    global game, step_game
    answ = message.text
    step_game += 1
    if answ.isdigit():
        answ = int(answ)
        if answ > hiden_num:
            bot.reply_to(message,'Перелёт!')
            bot.register_next_step_handler(message, process_game)
        elif answ < hiden_num:
            bot.reply_to(message,'Недалёт!')
            bot.register_next_step_handler(message, process_game)    
        elif answ == hiden_num:
            game = False
            bot.reply_to(message,f'Попал! Угадал {hiden_num} за {step_game} шагов.')
        else:
            bot.reply_to(message,'oops')
            bot.register_next_step_handler(message, process_game)        
    else:
        bot.reply_to(message,'Требуется число!')
        bot.register_next_step_handler(message, process_game)
    pass


bot.infinity_polling()


