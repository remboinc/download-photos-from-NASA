import os
from pathlib import Path
import requests
from dotenv import load_dotenv
from make_directory_and_download import make_dir_and_download_images


def get_nasa_image_links(nasa_token):
    api_url = 'https://api.nasa.gov/planetary/apod'
    number_of_photos = 30
    params = {'api_key': nasa_token, 'count': number_of_photos}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    nasa_images_url = []
    for url in response.json():
        nasa_images_url.append(url['url'])
    return nasa_images_url


def main():
    load_dotenv()
    safe_folder = Path('images')
    nasa_token = os.getenv('NASA_TOKEN')

    all_image_links = get_nasa_image_links(nasa_token)
    make_dir_and_download_images(all_image_links, safe_folder)



if __name__ == '__main__':
    main()