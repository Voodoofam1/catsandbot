from handlers.actions import history

def show_history(bot, message):
    '''показ истории действий пользователй в боте'''
    if history:
        bot.send_message(message.chat.id, '\n'.join(history))
    else:
        bot.send_message(message.chat.id,"активных действий не было")
