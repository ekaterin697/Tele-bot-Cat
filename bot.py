import telebot
from telebot import types	
import sys, os
import random

path = sys.argv[1]
bot = telebot.TeleBot("1237408271:AAGvN7X_WLOrrr5-JWO00wJiTeQ5mDlV0I8")

path_error_message = 'Путь к папке указан неправильно. Попробуйте перезапустить скрипт и указать верный путь'

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup()
	itembtn1 = types.KeyboardButton(text='Получить')
	markup.add(itembtn1)
	bot.reply_to(message, 'Здравствуйте! Этот бот будет высылать Вам фото котеек)', reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == 'Получить')
def send_something(message):
	try:
		files = os.listdir(path=path)
	except:
		print(path_error_message)
		bot.reply_to(message, path_error_message)
	choice = random.choice(files)
	print(choice)
	try:
		if path[-1] == '/':
			photo = open(path + choice, 'rb')
			bot.send_photo(message.chat.id, photo)
			return
		photo = open(path + '/' + choice, 'rb')
		bot.send_photo(message.chat.id, photo)
	except:
		bot.send_photo(message.chat.id, 'Упс.. что-то пошло не так.. Попробуйте перезапустить скрипт')

bot.polling()