from os import path
import os

counter = 0
cwd = os.getcwd()
print(cwd)
os.chdir('Splitted_Audio_Files')
trans = "Transcribed{}.txt"
cwd = os.getcwd()
print(cwd)
while os.path.isfile(trans):
    counter += 1
    trans = trans.format(counter)
    print(trans)