import time
import telegram

bot = telegram.Bot(token="7956675929:AAGLMzixq2kNV1P2a6benbzWf_8Z7vuGcOo")

last_id = 0

while True:
    updates = bot.getUpdates(offset=last_id)
    for update in updates:
        update_id = update.update_id
        last_id = update_id + 1
        chat_id = update.message.chat_id
        text = update.message.text

        bot.send_message(chat_id, text)
    time.sleep(1)