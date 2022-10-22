import os
from dotenv import load_dotenv
from make_directory_and_download import download_images, make_dir, take_all_images
from telegram_space_bot import bot_send_a_massage
from fetch_spacex_last_launch import fetch_spacex_last_launch
from take_nasa_images import take_nasa_images
from take_epic_images import take_epic_images


def main():
    load_dotenv()

    safe_folder = "/Users/ok_user/PycharmProjects/untitled3/images"
    nasa_token = os.getenv('NASA_TOKEN')
    nasa_images_url = take_nasa_images(nasa_token)
    image_links = fetch_spacex_last_launch()
    epic_images = take_epic_images(nasa_token)
    all_images = take_all_images(nasa_images_url, image_links, epic_images)

    make_dir(safe_folder)
    fetch_spacex_last_launch()
    take_nasa_images(nasa_token)
    download_images(all_images, safe_folder)
    take_epic_images(nasa_token)
    bot_send_a_massage()


if __name__ == '__main__':
    main()
