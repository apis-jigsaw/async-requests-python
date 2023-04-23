import aiohttp
import asyncio
import json
import time

async def fetch(url, params = {}):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params = params) as response:
            return await response.text()

async def get_artist(artist_name):
    url = "https://itunes.apple.com/search"
    
    params = {
        "term": artist_name,
        "entity": "album",
        "limit": 5,
        "sort": "recent",
    }
    response_text = await fetch(url, params = params)
    response_json = json.loads(response_text)
    matching_result = [result for result in response_json['results'] if result['artistName'] == artist_name]
    print(matching_result)

def get_artists(artist_names):
    return [get_artist(artist_name) for artist_name in artist_names]

async def main(artist_names):
    coros = get_artists(artist_names)
    await asyncio.gather(*coros)


artist_names = ['Billy Eilish', 'Dua Lipa', 'Lorde']
start = time.time()
if __name__ == "__main__":
    asyncio.run(main(artist_names))

end = time.time()
print(end - start)