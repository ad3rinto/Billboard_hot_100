import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
# from dotenv import load_dotenv

# load_dotenv()


<<<<<<< HEAD
=======
SPOTIPY_CLIENT_ID =os.environ.get('CLIENT_ID')
SPOTIPY_CLIENT_SECRET=os.environ.get('CLIENT_SECRET')
print(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
>>>>>>> 1d4bb6fc6541d802395ca339c2e6b1dd30b26445

SPOTIPY_CLIENT_ID =os.environ.get['CLIENT_ID']
SPOTIPY_CLIENT_SECRET=os.environ.get['CLIENT_SECRET']

print(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)

# year_of_travel = input("What year will you like to travel to ? YYY-MM-DD format please: ")
# # print(year_of_travel)

# URL = f"https://www.billboard.com/charts/hot-100/{year_of_travel}/"

# web_data = requests.get(URL)
# content = web_data.text

# soup = BeautifulSoup(content, "html.parser")
# # print(soup.prettify())

# song_name_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_name_spans]
# # print(song_names)

# song_artist_spans = soup.select("li ul li span")
# artist_names = [artist.getText().strip() for artist in song_artist_spans]
# # print(artist_names)
# new_artist_names = [item for item in artist_names if not item.isdigit()]
# # print(new_artist_names)
# pos = 1
# for (title, artist) in zip(song_names, new_artist_names):
#     print(f"At position {pos} is: {title}\nArtist: {artist}\n")
#     pos += 1
