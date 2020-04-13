import os

videoUrl = "https://www.youtube.com/watch?v=13hL-aDEyrI"
finalCmd = "youtube-dl -x --audio-format mp3 "+videoUrl+" ./ressources/mizo"
print(finalCmd)
system(finalCmd)

