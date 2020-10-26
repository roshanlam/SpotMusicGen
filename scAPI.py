# SoundCloud's API
# Make sure you have soundcloud-lib installed
# For documenation of souncloud-lib use the links below
# https://pypi.org/project/soundcloud-lib/
# https://github.com/3jackdaws/soundcloud-lib

#
# To fetch a playlist example
# To-Do: Figure Out How To CRUD (Create Read Update and Delete) Playlists for Soundcloud
#

from sclib import SoundcloudAPI, Track, Playlist

api = SoundcloudAPI()
playlist = api.resolve('https://soundcloud.com/playlist_url')
assert type(playlist) is Playlist

for track in playlist.tracks:
    filename = f'./{track.artist} - {track.title}.mp3'
    with open(filename, 'wb+') as fp:
        track.write_mp3_to(fp)
