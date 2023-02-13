import telebot

data = open('TokenText.txt', mode='r', encoding='utf-8')
API_TOKEN = data.read()
data.close

bot = telebot.TeleBot(API_TOKEN, parse_mode=None)

@bot.message_handler(commands=['start','ыефке'])
def send_welcome(message):
	bot.reply_to(message, f"Привет {message.from_user.first_name} я бот тех поддержки, \nнабери /support и опиши проблему.")
	
@bot.message_handler(commands=['support'])
def send_welcome(message):
	bot.reply_to(message, "Сообщение для техподдержки:")	
	bot.register_next_step_handler(message, process_supp_send)


def process_supp_send(message):
	user_msg = f'{message.from_user.id}:{message.text}\n'
	file_name = f'log.txt'
	data = open(file_name, "a", encoding="utf-8")
	data.write(user_msg)
	data.close
	bot.reply_to(message,'Отправил.')

    

bot.infinity_polling()