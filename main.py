import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def make_dir(safe_folder):
    try:
        os.makedirs(safe_folder)
    except FileExistsError:
        print('Папка уже существует')
    return safe_folder


def fetch_spacex_last_launch():
    api_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(api_url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr']['original']
    return image_links


def download_images(all_images, safe_folder):
    for index, space_image in enumerate(all_images):
        path = urlparse(space_image).path
        extension = os.path.splitext(path)[1]
        image_name = f'space_image_{index}{extension}'
        filename = f'{safe_folder}/{image_name}'
        response = requests.get(space_image)
        with open(filename, 'wb') as file:
            file.write(response.content)


def take_nasa_images(nasa_token):
    api_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_token, 'count': 30}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    nasa_images_url = []
    for url in response.json():
        nasa_images_url.append(url['url'])
    return nasa_images_url


def take_epic_images(nasa_token):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': nasa_token}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    epic_images = []
    for data in response.json():
        date_time = data['date'].split()[0]
        year = list(date_time)[0] + list(date_time)[1] + list(date_time)[2] + list(date_time)[3]
        month = list(date_time)[5] + list(date_time)[6]
        day = list(date_time)[8] + list(date_time)[9]
        name_of_image = data['image']
        url = f'https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{name_of_image}.png'
        epic_images.append(url)
    return epic_images


def take_all_images(nasa_images_url, image_links, epic_images):
    all_images = nasa_images_url + image_links + epic_images
    return all_images


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
