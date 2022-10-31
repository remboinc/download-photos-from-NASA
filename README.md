# Download photos from NASA and SpaceX
The bot downloads photos of Nasa and SpaceX and posts them to the Telegram channel every 4 hours.
## How to use
Clone the repository.

    git clone https://github.com/remboinc/download-photos-from-NASA.git

To get photos through the NASA API, you need to get a NASA token. To generate it, go to https://api.nasa.gov.

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
Creates a directory. Sends a request to the SpaseX and NASA APIs. Downloads the resulting images to the created directory. Calls a telegram bot that publishes images from a selected directory every 4 hours. 

To run the script, change to the project directory, then type on the command line:

    python3 main.py

To stop the script, type Ctrl+c. KeyboardInterrupt error will be returned:

        time.sleep(14400)
     KeyboardInterrupt


## download_images.py
Creates a directory and downloads the resulting files into it.

To run the script, type on the command line:
    
    python3 download_images.py

## fetch_spacex_last_launch.py
Sends a request to the SpaceX API, downloads the resulting images and saves to the selected directory.

To run the script, type on the command line:

    python3 fetch_spacex_last_launch.py

## get_epic_image_links.py
Sends a request to the NASA API, downloads epic images and saves to the selected directory.

To run the script, type on the command line:

    python3 get_epic_image_links.py

## get_nasa_image_links.py
Sends a request to the NASA API, downloads the received images and saves to the selected directory.

To run the script, type on the command line:

    python3 get_nasa_image_links.py

## telegram_space_bot.py
Calls a telegram bot that publishes images from a selected directory every 4 hours. 

To run the script, type on the command line:

    python3 telegram_space_bot.py
    
If there are no images in the selected directory, the script will generate an error:
    
    FileNotFoundError: [Errno 2] No such file or directory: 'images'
    







