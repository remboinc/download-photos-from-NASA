import requests
from dotenv import load_dotenv
from download_photos_from_NASA.make_directory_and_download import download_images, make_dir


def fetch_spacex_last_launch():
    api_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(api_url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr']['original']
    return image_links


def main():
    load_dotenv()
    safe_folder = "/Users/ok_user/PycharmProjects/untitled3/images"
    all_images = fetch_spacex_last_launch()

    make_dir(safe_folder)
    fetch_spacex_last_launch()
    download_images(all_images, safe_folder)



if __name__ == '__main__':
    main()
