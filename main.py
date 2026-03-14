import os
from dotenv import load_dotenv
from handlers.start import start
import telebot

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    start(bot, message)

if __name__ == '__main__':
    print("бот работает")
    bot.polling()
