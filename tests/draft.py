import time, eyed3

audiofile = eyed3.load("song.mp3")
print( audiofile.tag.artist )
print( audiofile.tag.album )
print( audiofile.tag.album_artist )
print( audiofile.tag.title )
print( audiofile.tag.track_num.count)

#Import os Library
import os

#print all entries in current directory
print (os.listdir())