import telebot
from random import randint as ri


data = open('TokenText.txt', mode='r', encoding='utf-8')
API_TOKEN = data.read()
data.close
game = False
hiden_num = 0
bot = telebot.TeleBot(API_TOKEN, parse_mode=None)

# Handles all text messages that contains the commands '/start' or '/help'
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f"Привет, {message.from_user.first_name}")

@bot.message_handler(content_types=['text'])
def log_chat(message):
    data = open('message_log.txt', 'a', encoding='utf-8')
    text = f'{message.from_user.id} {message.from_user.first_name} {message.from_user.last_name}: {message.text}\n'
    data.writelines(text)
    data.close


bot.infinity_polling()

    