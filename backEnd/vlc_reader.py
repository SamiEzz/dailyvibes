import vlc
from time import sleep
def play_instance(source):
    status = 0
    i = vlc.Instance()
    media_player = i.media_player_new()
    media_player.set_mrl(source)
    media_player.play()
    return status

i = vlc.Instance()
media_player = i.media_player_new()
media_player.set_mrl('./ressources/13hL-aDEyrI.mp3')
media_player.play()
sleep(600)