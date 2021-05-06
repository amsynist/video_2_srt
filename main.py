import moviepy.editor
from pydub import AudioSegment
from pydub.utils import make_chunks
from pathlib import Path
from functions import Speech2txt
import time
import os
import shutil
# Extracts Audio from  Video 

cwd = os.getcwd()
vid = moviepy.editor.VideoFileClip(r"dict.mp4")
audio = vid.audio
try:
    os.mkdir('Extracted_Audio')
    
except FileExistsError:
    shutil.rmtree('Extracted_Audio', ignore_errors=True) 
    os.mkdir('Extracted_Audio')
audio.write_audiofile(r"Extracted_Audio\Extracted_Audio_Files.wav")
print("Extracted Audio from Video....")
time.sleep(0.5)
# Slicing Extracted Audio into Equal Chunks/Parts

myaudio = AudioSegment.from_file(r"Extracted_Audio\Extracted_Audio_Files.wav" , "wav") 
chunk_length_ms = 50000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

try:
    os.mkdir('Splitted_Audio_Files')
except FileExistsError:
    shutil.rmtree('Splitted_Audio_Files', ignore_errors=True)
    os.mkdir('Splitted_Audio_Files')

os.chdir('Splitted_Audio_Files')

#Export all of the individual chunks as .mp3 files
for i, chunk in enumerate(chunks):
    chunk_name = "Split_Audio_Part_{0}.wav".format(i+10)
    print (f"Splitted And Exporting... [{chunk_name}]")
    time.sleep(0.2)
    chunk.export(chunk_name, format="wav")

print("Recognizing Speech from Splitted Audio Files")

mydir = Path.cwd()
for file in mydir.glob('*.wav'):
    convert = file.name
    time.sleep(2)
    Speech2txt(convert)
    time.sleep(3)
    print (f"Recognized speech of file - {convert}")

print("Recognized speech is converted and stored in 'Splitted_Audio_Files/Transcribed.txt' File")
