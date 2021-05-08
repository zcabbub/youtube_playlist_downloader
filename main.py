import moviepy.editor as mp
from pytube import YouTube
from pytube import Playlist
import os
import re

steppy = "https://www.youtube.com/playlist?list=PLnepKAkC61SMmPReCOXHPDtcxMji5OL2S"
tribal = "https://www.youtube.com/playlist?list=PLnepKAkC61SO46-joCO1Rd0pbDGUU4G7l"
highers = "https://www.youtube.com/playlist?list=PLnepKAkC61SPIMSZ6j9OtvuQiGs0vfbLQ"
supreme = "https://www.youtube.com/playlist?list=PLnepKAkC61SNUNzi_kjrJFQoCsvz9rpd5"
sunny = 'https://www.youtube.com/playlist?list=PLnepKAkC61SO5ndNB4LCHY9rL8TAtoKAp'
weird = "https://www.youtube.com/playlist?list=PLnepKAkC61SPMBL0RNsjv7_SDTeDqpWgt"
groovie = "https://www.youtube.com/playlist?list=PLnepKAkC61SPe09W3N9pHXnANTvQVoTEH"
elrow = "https://www.youtube.com/playlist?list=PLnepKAkC61SMS2Z8zvEYCqokeRfl7FiRT"
garage = "https://www.youtube.com/playlist?list=PLnepKAkC61SMQlt2Q9yKGHJ_h0DFYRfpq"

enders = "https://www.youtube.com/playlist?list=PLnepKAkC61SPzdSjQ6hyssDqDQrnqTLkE"
beginners = "https://www.youtube.com/playlist?list=PLnepKAkC61SMIBWNxX9MDFlxqOQs6kSLN"
overwhelming = "https://www.youtube.com/playlist?list=PLnepKAkC61SMRN7Y400TE4THcCtlEmJHX"
relief = 'https://www.youtube.com/playlist?list=PLnepKAkC61SMXWuHNMUnhLCIKBD7FrNTM'

known = "https://www.youtube.com/playlist?list=PLnepKAkC61SO7vVPWJje4t1qWAVpI61uH"
dnb = "https://www.youtube.com/playlist?list=PLnepKAkC61SME9-gfFLXfQmIuATBiFQ9e"

mid = 'https://www.youtube.com/playlist?list=PLnepKAkC61SN_b33sQGJBpdfuGIgVsjYp'
min_chill = "https://www.youtube.com/playlist?list=PLnepKAkC61SPJaaKTY4hrqvdw_IuSGZOO"

#sunny nu merge
playlists = [beginners]

def convert(folder):
    print("Converting from mp4 to mp3...")
    for file in os.listdir(folder):
        if re.search('mp4', file):
            mp4_path = os.path.join(folder, file)
            video = mp.AudioFileClip(mp4_path)
            mp3_path = os.path.join(folder, os.path.splitext(file)[0] + '.mp3')
            video.write_audiofile(mp3_path)
            os.remove(mp4_path)
    print("Converting DONE.")
    print(f"{playlist} DONE.".format(playlist=folder))

for url in playlists:
    playlist = Playlist(url)
    folder = playlist.title

    # check if the playlist was already downloaded
    try:
        os.mkdir(folder)
        print(f"Downloading playlist '{playlist}'...".format(playlist=folder))
        for song in playlist:
            try:
                YouTube(song).streams.filter(only_audio=True).first().download(folder)
            except:
                print("Error at '{song}' with link: {link}".format(song=song.title, link=song))
        print("Downloading DONE.")
        convert(folder)
    except:
        print("Playlist already downloaded.")
        print("Checking for differences...")
        differences=0

        for song in playlist:
            song_yt = YouTube(song)
            song_title = song_yt.title
            if '.' in song_title:
                song_title = song_title.replace('.', '')
            song_name = song_title + ".mp3"

            if not os.path.exists(os.path.join(folder, song_name)):
                song_yt.streams.filter(only_audio=True).first().download(folder)
                differences = differences+1

        print("Downloaded {x} additional songs.".format(x=differences))
        convert(folder)

print("Download successful")