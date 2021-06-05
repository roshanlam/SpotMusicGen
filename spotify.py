import requests
import urllib.parse

class SpotifyUser(object):
	def __init__(self, token):
		self.token = token

	def search_song(self, artist, track):
		q = urllib.parse.quote(f'{artist} {track}')
		url = f'https://api.spotify.com/v1/search?q={q}&type=track'
		res = requests.get(url, headers={
			'Content-Type': 'application/json', 
			'Authorization': f'Bearer {self.token}'
		})

		res_json = res.json()

		results = res_json['tracks']['items']
		if results:
			return results[0]['id']
		else:
			raise Exception(f'No song {track} was found by {artist}')

	def addToSpotify(self):
		url = 'https://api.spotify.com/v1/me/tracks'
		song_id = ''
		res = requests.put(
			url, json={'ids': [song_id]},
			headers = {
				'Content-Type': 'application/json',
				'Authorization': f'Bearer {self.token}'
			}
		)

		return res.ok