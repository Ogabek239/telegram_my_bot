import time
import telegram

bot = telegram.Bot(token="8016350842:AAEvU0fcRkhyo9qzKCBCZwIwIBWE3KUKeW4")

last_id = 0

while True:
    updates = bot.getUpdates(offset=last_id)
    for update in updates:
        update_id = update.update_id
        last_id = update_id + 1

        if update.message:
            chat_id = update.message.chat_id

            if update.message.text:
                bot.send_message(chat_id=chat_id, text=update.message.text)

            elif update.message.audio:
                bot.send_audio(chat_id=chat_id, audio=update.message.audio.file_id)

            elif update.message.video:
                bot.send_video(chat_id=chat_id, video=update.message.video.file_id)

            elif update.message.sticker:
                bot.send_sticker(chat_id=chat_id, sticker=update.message.sticker.file_id)

    time.sleep(1)
