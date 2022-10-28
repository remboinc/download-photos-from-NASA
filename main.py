import itertools
import os
from pathlib import Path
from dotenv import load_dotenv
from make_directory_and_download import make_dir_and_download_images
from telegram_space_bot import send_a_message_using_a_bot
from fetch_spacex_last_launch import fetch_spacex_last_launch
from get_nasa_image_links import get_nasa_image_links
from get_epic_image_links import get_epic_image_links


def main():
    load_dotenv()

    safe_folder = Path('images')
    nasa_token = os.getenv('NASA_TOKEN')
    telegram_bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHANNEL_ID')

    nasa_images_url = get_nasa_image_links(nasa_token)
    image_links = fetch_spacex_last_launch()
    epic_images = get_epic_image_links(nasa_token)
    all_image_links = list(itertools.chain(nasa_images_url, image_links, epic_images))
    make_dir_and_download_images(all_image_links, safe_folder)
    send_a_message_using_a_bot(telegram_bot_token, chat_id)


if __name__ == '__main__':
    main()
