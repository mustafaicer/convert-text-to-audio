from gtts import gTTS
import os

text = input("Enter text : ")
audio_file = gTTS(text=text, lang='tr')
audio_file.save("converted.mp3")
os.system("start converted.mp3")