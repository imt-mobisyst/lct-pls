import time 
from playsound3 import playsound

# You can play sounds in the background
sound = playsound("./mp3/01-nonpoint-in_the_air_tonight.mp3", block=False)

# and check if they are still playing
if sound.is_alive() :
    print("Sound is playing!")
    time.sleep( 5.0 )

# and stop them whenever you like.
sound.stop()
