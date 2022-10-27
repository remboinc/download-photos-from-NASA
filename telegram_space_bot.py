import random
from pathlib import Path
import telegram
from dotenv import load_dotenv
import os
import time


def send_a_message_using_a_bot(telegram_bot_token, chat_id):
    bot = telegram.Bot(telegram_bot_token)
    while True:
        path = Path('images')
        images = os.listdir(path=path)
        images = list(images)
        random.shuffle(images)
        for image in images:
            photos_directory = os.path.join(path, image)
            with open(photos_directory, 'rb') as photo:
                bot.send_document(chat_id=chat_id, document=photo)
            time.sleep(14400)


def main():
    load_dotenv()

    telegram_bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHANNEL_ID')

    send_a_message_using_a_bot(telegram_bot_token, chat_id)


if __name__ == '__main__':
    main()
