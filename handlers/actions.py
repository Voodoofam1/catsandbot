import os

history = []

def handle_actions(bot, message):
    '''выполнение действие при нажатии на кнопку пользователем: погладить и обнять кота '''
    text = message.text

    if "погладить" in text:
        history.append("погладить кота")
        photo_path = os.path.join("media", "cat1.gif")
        if os.path.exists(photo_path):
            with open(photo_path, "rb") as f:
                bot.send_animation(message.chat.id, f, caption="кот доволен")

    elif "обнять" in text:
        history.append("обнять кота")
        photo_path = os.path.join("media", "cat2.gif")
        if os.path.exists(photo_path):
            with open(photo_path, "rb") as f:
                bot.send_animation(message.chat.id, f, caption="кот счастлив")
