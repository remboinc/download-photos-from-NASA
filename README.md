# Download photos from NASA and SpaceX
The bot downloads photos of Nasa and SpaceX and posts them to the Telegram channel every 4 hours.
## How to use
Clone the repository.

    git clone https://github.com/remboinc/download-photos-from-NASA.git

To get photos through the NASA API, you need to get a NASA token. To generate it, go to https://api.nasa.gov.
Token будет выглядеть так:

In order for a telegram bot to send photos, you need to create it and also get a token. Detailed instructions can be found at the link https://core.telegram.org/bots.
Make the bot the administrator of your telegram channel.

Create an .env file and set the variables:

* NASA_TOKEN=YOUR_TOKEN, where instead of YOUR_TOKEN paste the received NASA token. 
* BOT_TOKEN variable, write the received telegram bot token.
* TELEGRAM_CHANNEL_ID

Example: 

    NASA_TOKEN=1745hjdewdke743yrh349jdi39i231da7
    BOT_TOKEN=1234556789:AAA-GJHhj7887hjTFN4dZWbtJnDM5-WvpSvc
    TELEGRAM_CHANNEL_ID=@example_channel
    
Everything is ready to launch.
    
## main.py 
Creates a directory. Sends a request to the SpaseX and NASA APIs. Downloads the resulting images to the created directory. Calls a telegram bot that publishes images from the selected directory.

## make_directory_and_download.py
Creates a directory and downloads the resulting files into it.

## fetch_spacex_last_launch.py
Sends a request to the SpaceX API, downloads the resulting images and saves to the selected directory.

## take_epic_images.py 
Sends a request to the NASA API, downloads epic images and saves to the selected directory.

## take_nasa_images.py
Sends a request to the NASA API, downloads the received images and saves to the selected directory.









