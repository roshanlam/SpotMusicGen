import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests 
import youtube_dl


# these imports below are from files
from expec import ResponseException
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
     
