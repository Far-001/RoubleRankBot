from dotenv import load_dotenv
import os
import telebot

load_dotenv()

TOKEN = os.environ.get('TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    print('bot_started')
    bot.infinity_polling()
