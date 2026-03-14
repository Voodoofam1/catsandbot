import os
from keyboards.menu import menu


def start(bot, message):
    ''' запуск бота через команду старт'''
    photo_path = os.path.join("media", "cat.jpg")

    if os.path.exists(photo_path):
        with open(photo_path, "rb") as f:
            bot.send_photo(message.chat.id, photo=f,caption="привет ✌")
    else:
        bot.send_message(message.chat.id, "привет фотки нет😊")

    bot.send_message(message.chat.id,"выбери действие", reply_markup=menu)

