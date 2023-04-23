import requests
import json
import time




def get_artist(artist_name):
    url = "https://itunes.apple.com/search"
    
    params = {
        "term": artist_name,
        "entity": "album",
        "limit": 5,
        "sort": "recent",
    }
    response = requests.get(url, params = params)
    response_json = response.json()
    matching_result = [result for result in response_json['results'] if result['artistName'] == artist_name]
    print(matching_result)

def get_artists(artist_names):
    return [get_artist(artist_name) for artist_name in artist_names]

def main(artist_names):
    coros = get_artists(artist_names)

start = time.time()
artist_names = ['Billy Eilish', 'Dua Lipa', 'Lorde', 'Pink Floyd', 'Paul Simon']

main(artist_names)

end = time.time()
print(end - start)