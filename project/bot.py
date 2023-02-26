import telebot
from telebot import types
import controll
import os
from time import sleep


bot = telebot.TeleBot("")
markup = InlineKeyboardMarkup()
markup.row_width = 1
markup.add(InlineKeyboardButton("обновить", callback_data="update"),InlineKeyboardButton("полив", callback_data="water"),InlineKeyboardButton("фото", callback_data="cam"))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот для работы с теплицей.")

def control():
    t,h = controll.get_info()
    bot.send_message(message.chat_id,f"температура:{t}\nвлажность:{h}",markup)

def send_photo(message):
    controll.make_photo()
    bot.send_photo(message.chat.id,open("photo.jpg","rb"))
    os.remove("photo.jpg")
    control()


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "update":
        control()
    elif call.data == "water":
        bot.send_message(message.chat.id,"минут полива(только целые числа):")
        sleep(10)
        time = message.text
        try:
            controll.water(time)
            
        except ValueError:
            bot.send_message(message.chat.id,"произошла ошибка")
    elif call.data == "cam":
        send_photo(call.message)
