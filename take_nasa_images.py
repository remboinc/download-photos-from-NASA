import os
import requests
from dotenv import load_dotenv
from download_photos_from_NASA.make_directory_and_download import download_images, make_dir

def take_nasa_images(nasa_token):
    api_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_token, 'count': 30}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    nasa_images_url = []
    for url in response.json():
        nasa_images_url.append(url['url'])
    return nasa_images_url


def main():
    load_dotenv()
    safe_folder = "/Users/ok_user/PycharmProjects/untitled3/images"
    nasa_token = os.getenv('NASA_TOKEN')
    all_images = take_nasa_images(nasa_token)

    make_dir(safe_folder)
    take_nasa_images(nasa_token)
    download_images(all_images, safe_folder)



if __name__ == '__main__':
    main()