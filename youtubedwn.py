#!/usr/bin/env python
# coding: utf-8

import os


videoUrl = "https://www.youtube.com/watch?v=spCdFMnQ1Fk"
finalCmd = "youtube-dl -x --audio-format mp3 "+videoUrl+" ./ressources/bella"
print(finalCmd)
#system(finalCmd)

