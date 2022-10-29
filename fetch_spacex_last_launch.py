from pathlib import Path
import requests
from download_images import download_images


def fetch_spacex_last_launch():
    api_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(api_url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr']['original']
    return image_links


def main():
    safe_folder = Path('images')

    all_image_links = fetch_spacex_last_launch()
    download_images(all_image_links, safe_folder)


if __name__ == '__main__':
    main()
