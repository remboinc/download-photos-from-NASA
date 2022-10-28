import os
from urllib.parse import urlparse
import requests


def make_dir_and_download_images(all_image_links, safe_folder):
    os.makedirs(safe_folder, exist_ok=True)
    for index, space_image in enumerate(all_image_links):
        path = urlparse(space_image).path
        extension = os.path.splitext(path)[1]
        image_name = f'space_image_{index}{extension}'
        filename = os.path.join(safe_folder, image_name)
        response = requests.get(space_image)
        with open(filename, 'wb') as file:
            file.write(response.content)