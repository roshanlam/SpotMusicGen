import os

import requests 
import youtube_dl 
import google_auth_oauthlib.flow
import googleapiclient.discovery

class Playlist(object):
	def __init__(self, id, title):
		self.id = id
		self.title = title

class Song(object):
	def __init__(self, artist, track):
		self.artist = artist
		self.track = track 

class YouTubeUser(object):
	def __init__(self):
		scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
		# Disable OAuthlib's HTTPS verification when running locally.
        # DO NOT -> leave this option enabled in production.
		os.environ["OAUTHLIB_INSTANCE_TRANSPORT"] = "1"
		service_name = "youtube"
		version = "v3"

		f = google_auth_oauthlib.flow.InstalledAppFlow.from_user_secret_files(scopes)
		credentials = flow.run_console()
		youtube_user = googleapiclient.discovery.build(service_name, version, credentials=credentials)
		self.youtube_user = youtube_user

	def get_playlists(self):
		request = self.youtube_user.playlists().list(part="id, snippet", maxResults=100, mine=True)
		res = request.execute()
		pls = [Playlist(item['id'], item['snippet']['title']) 
		for item in res['items']]
		return pls

	def getSongsFromVideos(self):
		songs = []
		res = self.youtube_user.playlistitems().list(
			playlistId = playlist_id, 
			part="id, snippet",
			maxResults = 100	
		)
		res = requests.execute()

		for item in res['items']:
			song_id = item['snippet']['resourceId']
			artist, track = self.getArtistAndTracK(song_id)
			if artist and track:
				songs.append(Song(artist, track))
		return songs



	def getArtistAndTrack(self):
		song_id = ''
		utube_url = f'https://www.youtube.com/watch?v={song_id}'
		song = youtube_dl.YoutubeDL({'quiet': True}).extract_info(
			utube_url, download = False
		)

		artist = song['artist']
		track = song['track']
		return artist, track







