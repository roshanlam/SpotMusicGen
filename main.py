import os 
from spotify import SpotifyUser
from youtube import YoutubeUser 
#from soundcloud import ScUser
#class Main:

# Recoded the entire program to reduce the lines of code written.
# To-DO: Write tests and implement design pattern(s)
def main():
    yt_user = YoutubeUser('user_secret.json')
    sp_user = SpotifyUser(os.getenv('SPOT_AUTH_TOKEN'))
    # pls = playlists
    pls = yt_user.get_playlists()

    for i, playlist in enumerate(pls):
        print(f'{i}: {playlist.title}')
try:
    c = int(input('Enter your Choice'))
except ValueError:
    print('You can only input a integer you stupid')
    c_playlist = pls[c]
    print(f'You Choose: {c_playlist.title}')
    songs = yt_user.get_playlists(c_playlist.id)
    print(f'Trying to add {len(songs)}')

    for song in songs:
        sp_song_id = sp_user.search_song(song.artist, song.track)
        if sp_song_id:
            added_song = sp_user.addToSpotify(sp_song_id)
            if added_song:
                print(f"Added {song.artist} - {song.track} to your Spotify Liked Songs")
        

if __name__ == '__main__':
    main()