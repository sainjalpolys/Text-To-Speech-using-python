# Import the required module for text 
# to speech conversion
from gtts import gTTS
# This module is imported so that we can 
# play the converted audio
import os
from pygame import mixer # Load the required library
import time

language = 'en'
myobj = gTTS(text='Type Something to Speak', lang=language, slow=False)
myobj.save("welcome.mp3")
mixer.init()
mixer.music.load('welcome.mp3')
mixer.music.play()
while mixer.music.get_busy():		
	time.sleep(1)
os.remove('welcome.mp3')
# The text that you want to convert to audio
mytext = raw_input("Type Something to Speak!\n>")

while(mytext!='exit') :
	# Language in which you want to convert
	# Passing the text and language to the engine, 
	# here we have marked slow=False. Which tells 
	# the module that the converted audio should 
	# have a high speed
	myobj = gTTS(text=mytext, lang=language, slow=False) 
	myobj.save("welcome.mp3")
	# Playing the converted file
	mixer.init()
	mixer.music.load('welcome.mp3')
	mixer.music.play()
	while mixer.music.get_busy():		
		time.sleep(1)
	os.remove('welcome.mp3')
	mytext = raw_input("Type Something to Speak!\n>")
print"Exiting . . "	
myobj = gTTS(text=mytext+'ing from the program', lang=language, slow=False)
myobj.save("welcome.mp3")
mixer.init()
mixer.music.load('welcome.mp3')
mixer.music.play()
while mixer.music.get_busy():		
	time.sleep(1)
os.remove('welcome.mp3')