import os
from datetime import date
from pathlib import Path
import requests
from dotenv import load_dotenv
from make_directory_and_download import download_images


def get_epic_image_links(nasa_token):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': nasa_token}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    epic_images = []
    for date_and_time in response.json():
        just_date = date_and_time['date'].split()[0]
        datetime = date.fromisoformat(just_date).timetuple()
        (tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst) = datetime
        image_name = date_and_time['image']
        url = f'https://epic.gsfc.nasa.gov/archive/natural/{tm_year}/{tm_mon}/{tm_mday}/png/{image_name}.png'
        epic_images.append(url)
    return epic_images


def main():
    load_dotenv()
    safe_folder = Path('images')
    nasa_token = os.getenv('NASA_TOKEN')

    all_image_links = get_epic_image_links(nasa_token)
    download_images(all_image_links, safe_folder)


if __name__ == '__main__':
    main()