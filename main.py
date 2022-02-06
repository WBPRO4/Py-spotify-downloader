import os
import logging
import time
import tekore as tk
import pytube

x = 0
songs = []
user_data=[]
token = ""
Client_id = "86ff07cb4d14467eb1558bb90cfc8dfd"
Redirect_uri = "http://127.0.0.1/"
Client_secret = "f7bc86a944984a13bf9402cece9f61b8"
enable_debug = False
cls = lambda: os.system("cls")
kill_nginx = lambda: os.system("taskkill /im nginx.exe /f")
conf = (Client_id, Client_secret, Redirect_uri)
token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)

# set the modules logger so we only get crtitcal messages this will make it easier to make a pretty logger for me and to do debug messages in the main file
loggers_to_disable = ["requests", "urllib3", "httpx", "pytube"]
for module in loggers_to_disable:   
    logger = logging.getLogger(module)
    logger.setLevel(logging.CRITICAL)

if enable_debug:
    logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')
    logging.debug("Enabled Debug output!")
else:
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


logging.info("Starting Auth")
logging.debug(f"using client id: {Client_id}\n using client secret: {Client_secret}\n redirect uri is: {Redirect_uri}")

spotify = tk.Spotify(token)

# get the userid
# we will need this for some playlist operations
user_data.append(spotify.current_user().id)
user_data.append(spotify.current_user().display_name)


playlists = spotify.playlists(user_data[0]).items
playlist_IDs = []

for lists in playlists:
    playlist_IDs.append(playlists[x].id)
    x = x+1

x = 0

def SpotifyPlaylistScrape(ID):
    list_offset = 0
    # we only scrape up to 500 songs by deafult change the value below to change this behaviour
    while list_offset != 500:
        playlist = spotify.playlist_items(ID, as_tracks=False, limit=100, offset=list_offset)
        
        for item in playlist.items:
            logging.debug(item.track.name)
            songs.append(f"{item.track.artists[0].name} - {item.track.name}")

        list_offset = list_offset + 100


for ID in playlist_IDs:
    logging.debug(playlist_IDs[x])
    SpotifyPlaylistScrape(playlist_IDs[x])
    x = x+1

# remove duplicates
songs = set(songs)
songs = list(songs)


# youtube logic starts here 

logging.info("the following bangers will be downloaded:\n")
time.sleep(1.5)
for banger in songs:
    logging.info(banger)

logging.info(f"All together {len(songs)} fire songs will be downloaded")
logging.info("Is that okay? [y/n]")
anwser = input()

if anwser.lower() == "y":
    logging.info("Okay Scraping YouTube Now!")
    logging.warning("The Deafult beahviour is to get the first result")
    logging.warning("Note that this may mean that u down always get what you want")
    for banger in songs:
        logging.info(f"looking for {banger}")
        s = pytube.Search(banger)
        logging.info(f"first result is: {s.results[0].title}")
        logging.info(f"found {len(s.results)} on the first page")
        # And here's where the magic happens 
        try: 
            s.results[0].streams.filter(only_audio=True)[0].download()
        except pytube.exceptions.AgeRestrictedError:
            y = y+1
            if y != 4:
                s.results[0].streams.filter(only_audio=True)[y].download()
            else:
                ...
    logging.info(f"Downloaded len(songs) from youtube Sucessfully!")
    logging.info(f"Also fuck your family this was very fucking hard to make")
    logging.info("Press enter to exit you fucker!")
    input()
    kill_nginx()
    exit(1)

elif anwser.lower() == "n":
    logging.info("Okay! Exiting!")
    kill_nginx()
    exit(1)

else:
    logging.error("invalid input!")

kill_nginx()