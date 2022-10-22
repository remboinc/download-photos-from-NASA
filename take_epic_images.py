import os
import requests
from dotenv import load_dotenv
from download_photos_from_NASA.make_directory_and_download import download_images, make_dir


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


def main():
    load_dotenv()
    safe_folder = "/Users/ok_user/PycharmProjects/untitled3/images"
    nasa_token = os.getenv('NASA_TOKEN')
    all_images = take_epic_images(nasa_token)

    make_dir(safe_folder)
    take_epic_images(nasa_token)
    download_images(all_images, safe_folder)



if __name__ == '__main__':
    main()