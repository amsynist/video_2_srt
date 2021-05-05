
import speech_recognition as speecher
from os import path
import os
def Speech2txt(filename):
    rec = speecher.Recognizer()
    with speecher.AudioFile(filename) as source:
        audio_data = rec.record(source)
        # recognize (convert from speech to text)
        text = rec.recognize_google(audio_data)
        with open('Transcribed.txt',mode ='a') as file:
            file.write("\n") 
            file.write("------------------------REC-SPEECH----------------------") 
            file.write("\n") 
            file.write(text) 
