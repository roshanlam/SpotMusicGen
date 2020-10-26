import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests 
import youtube_dl


from exceptions import ResponseException
from secrets import spotify_token, spotify_user_id


    class Main: 
      def __int__(self): 
          self.youtube_client = self.get_youtube_client()
          self.all_song_info = {}
      
      def get_youtube_client(self):
        # Do not leave this line below enabled in Production, this basically disable's OAuthlib's HTTPS Verification when running locally. 
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        
    api_service_name = "youtube"
    api_verison = "v1"
    
    # Client's Secret Info will be in client_secret.json
    client_secrets_file = "client_secret.json"
    
    # Get the credentials and create an API (client)
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
    
    credentials = flow.run_console()
    
    # YouTube Data API
    youtube_client = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)
      return youtube_client
      
    def get_liked_videos(self): 
        """ Gets all the liked videos & creates a list of important songs """
         request = self.youtube_client.videos().list(
         part="snippet, contentDetails, statistics", myRating="like")

    response = request.execute()
    
    # Gets Users Playlist with the Query Songs
    def get_users_playlist(self):
        requestPlaylist = youtube.search().list(
        part="snippet",
        maxResults=100,
        q="Songs")
       
    PlaylistReponse = request.execute()
    
    
    # collects each video and its important info.
    for item in response["items"]
        video_title = item["snippet"]["title"]
        youtube_url = "https://www.youtube.com/watch?v={}".format(
         item["id"]
        )
        
        # using youtube_dl to collect the song's name & artist
        video = youtube_dl.YoutubeDL({}).extract_info(
            youtube_url, download=False)
        
        song_name = video["track"]
        artist = video["artist"]
        
        if song_name is not None and artist is not None:
   # saves all the important info and skips any missing song and/or artist
         self.all_song_info(video_title) = {
             "youtube_url": youtube_url, 
             "song_name": song_name, 
             "artist": artist, 
             
        # Get the uri since its an easy way to put the song on into the playlist
             "spotify_uri": self.get_spotify_uri(song_name, artist)
        
         }   
             
             
        def create_playlist(self): 
            request_body = json.dumps({
                "name": "USpot",
                "description": "All your favorite youtube videos",
                "public": True
            })
            
            query = "https://api.spotify.com/v1/users/{}/playlists".format(
                spotify_user_id) 
            response = requests.post(
                query, 
                data=request_body,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(spotify_token)
                }
            )
         
        response_json = response.json()
            
           # playslist id
        def get_spotify_uri(self,song_name, artist):
            query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # only use the first song
        uri = songs[0]["uri"]
        return uri
            
        
        
       def add_song_to_playlist(self):
        """Add all the songs into a new Spotify playlist"""
        self.get_liked_videos()

        # collect all of uri
        uris = [info["spotify_uri"]
                for song, info in self.all_song_info.items()]

        # create a new playlist
        playlist_id = self.create_playlist()

        # add all songs into the new playlist
        request_data = json.dumps(uris)

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            playlist_id)

        response = requests.post(
            query,
            data=request_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        
        
        # check for valid response status
        if response.status_code != 200:
            raise ResponseException(response.status_code)

        response_json = response.json()
        return response_json


        if __name__ == '__main__':
           cp = Main()
           cp.add_song_to_playlist()
