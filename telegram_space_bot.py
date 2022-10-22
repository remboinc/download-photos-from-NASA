import random
import telegram
from dotenv import load_dotenv
import os
import time


def bot_send_a_massage():
    token = os.getenv('BOT_TOKEN')
    bot = telegram.Bot(token)
    chat_id = '-1001650514384'
    while True:
        path = '/Users/ok_user/PycharmProjects/untitled3/images'
        images = os.listdir(path=path)
        images = list(images)
        random.shuffle(images)
        for image in images:
            photos_directory = f'{path}/{image}'
            bot.send_document(chat_id=chat_id, document=open(photos_directory, 'rb'))
            time.sleep(14400)


def main():
    load_dotenv()
    bot_send_a_massage()


if __name__ == '__main__':
    main()
