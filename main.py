import telegram

bot = telegram.Bot(token='BOT TOKEN')

updates = bot.get_updates()


if updates:
    message = updates[-1].message
    if message.text:
        chat_id = message.chat.id
        text = message.text
        bot.send_message(chat_id=chat_id, text=text)