import requests
import requests

def get_last_five_albums(artist_name):
    base_url = "https://itunes.apple.com/search"
    params = {
        "term": artist_name,
        "entity": "album",
        "limit": 5,
        "sort": "recent",
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return [(album["collectionId"], album["collectionName"]) for album in data["results"]]
    else:
        print(f"Error: {response.status_code}")
        return None

def get_album_tracks(collection_id):
    base_url = "https://itunes.apple.com/lookup"
    params = {
        "id": collection_id,
        "entity": "song",
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return [track["trackName"] for track in data["results"] if track["wrapperType"] == "track"]
    else:
        print(f"Error: {response.status_code}")
        return None

artist_name = "Billie Eilish"
last_five_albums = get_last_five_albums(artist_name)

if last_five_albums:
    print(f"Last five albums by {artist_name} and their tracks:")
    for collection_id, album_name in last_five_albums:
        tracks = get_album_tracks(collection_id)
        print(f"{album_name}:")
        for track in tracks:
            print(f"  - {track}")
        print()
