import os
from urllib.parse import urlparse
import requests


def make_dir(safe_folder):
    try:
        os.makedirs(safe_folder)
    except FileExistsError:
        print('Папка уже существует')
    return safe_folder


def take_all_images(nasa_images_url, image_links, epic_images):
    all_images = nasa_images_url + image_links + epic_images
    return all_images


def download_images(all_images, safe_folder):
    for index, space_image in enumerate(all_images):
        path = urlparse(space_image).path
        extension = os.path.splitext(path)[1]
        image_name = f'space_image_{index}{extension}'
        filename = f'{safe_folder}/{image_name}'
        response = requests.get(space_image)
        with open(filename, 'wb') as file:
            file.write(response.content)