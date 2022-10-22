import os
import telegram
from dotenv import load_dotenv


def bot_send_a_massage():
    token = os.getenv('BOT_TOKEN')
    bot = telegram.Bot(token)
    chat_id = '-1001650514384'
    text = input('Кать, введи сообщение')
    image = '/Users/ok_user/PycharmProjects/untitled3/images/space_image_0.jpg'
    bot.send_message(chat_id=chat_id, text=text)
    bot.send_document(chat_id=chat_id, document=open(image, 'rb'))


def main():
    load_dotenv()
    bot_send_a_massage()


if __name__ == '__main__':
    main()
