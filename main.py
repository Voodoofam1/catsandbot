import os
from dotenv import load_dotenv
from handlers.start import start
from handlers.actions import handle_actions
import telebot

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    start(bot, message)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    handle_actions(bot, message)

if __name__ == '__main__':
    print("бот работает")
    bot.polling()
