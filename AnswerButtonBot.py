# -*- coding: utf-8 -*-
from dotenv import load_dotenv
import os
import telebot
from telebot import types

load_dotenv()
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(
        message.from_user.id,
        "👋 Привет! Я твой бот-помошник!",
        reply_markup=markup,
    )


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True
        )  # создание новых кнопок
        btn1 = types.KeyboardButton('Железный человек')
        btn2 = types.KeyboardButton('Капитан Америка')
        btn3 = types.KeyboardButton('Человек-паук')
        markup.add(btn1, btn2, btn3)
        bot.send_message(
            message.from_user.id,
            '❓ Выбери героя и узри его!',
            reply_markup=markup,
        )  # ответ бота

    elif message.text == 'Железный человек':
        bot.send_photo(
            message.from_user.id,
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzFnS6EIKfDep8cGgtTJSDdzEDLmdusWkHDQ&usqp=CAU'
        )

    elif message.text == 'Капитан Америка':
        bot.send_photo(
            message.from_user.id,
            'https://images.unian.net/photos/2021_04/thumb_files/1200_0_1619428200-4319.jpg'
        )

    elif message.text == 'Человек-паук':
        bot.send_photo(
            message.from_user.id,
            'https://readrate.com/img/pictures/basic/197/197482/1974822/w816-604a5449.jpg'
        )


bot.polling(none_stop=True, interval=0)
