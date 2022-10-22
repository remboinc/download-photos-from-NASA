import os
from dotenv import load_dotenv
from main import download_images, make_dir, fetch_spacex_last_launch, take_nasa_images, take_epic_images, take_all_images


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


if __name__ == '__main__':
    main()
