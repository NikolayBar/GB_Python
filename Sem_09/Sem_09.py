import telebot
from random import randint as ri

bot = telebot.TeleBot("TOKEN", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, как у тебя дела?")



# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['rand'])
def handle_start_help(message):
    num = str(ri(10,22))
    bot.reply_to(message, num)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()


