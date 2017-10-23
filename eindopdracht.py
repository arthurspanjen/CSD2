import simpleaudio as sa
import time
import datetime
from random import randint
import copy
from multiprocessing import Process
import sys
from midiutil import MIDIFile

KICK = sa.WaveObject.from_wave_file("808kick.wav")
BLIEP = sa.WaveObject.from_wave_file("808cow.wav")
JACKU = sa.WaveObject.from_wave_file("808clap.wav")

track=0
channel=9
Mtime=0
duration=0.25
bpm=120
velocity=100

MyMIDI = MIDIFile(2)
MyMIDI.addTempo(track,Mtime,bpm)


print("how many repititions?")
repetitions=input("-> ")
while repetitions.isdigit() == False:
    print("Please input integer.")
    repetitions=input("-> ")
repetitions=int(repetitions)

listKick=[]
listSnare=[]
listMisc=[]

kickPlaced=0
snarePlaced=1
miscPlaced=0

steps=16
for x in range(steps):
    if x%2==0:
        if x == 0:
            listKick.append(0)
            kickPlaced=1
        if x > 0:
            if kickPlaced==1:
                kickPlaced=0
            elif kickPlaced==0:
                if randint(0, 1) > 0:
                    listKick.append(x)
                    kickPlaced=1

for x in range(steps):
    if x%2==0:
        if x == 4:
            listSnare.append(x)
            snarePlaced=1
        if x !=  4:
            if snarePlaced==1:
                snarePlaced=0
            elif snarePlaced==0:
                if randint(0, 1) > 0:
                    listSnare.append(x)
                    snarePlaced=1

for x in range(steps):
    if miscPlaced==1:
        miscPlaced=0
    elif miscPlaced==0:
        if randint(0,1)>0:
            listMisc.append(x)
            miscPlaced=1
    

MyMIDI.addTimeSignature(track, 0, steps, 4, 24)
playListMisc=copy.copy(listMisc)
playListKick=copy.copy(listKick)
playListSnare=copy.copy(listSnare)

def playSequence():
    playListMisc=copy.copy(listMisc)
    playListKick=copy.copy(listKick)
    playListSnare=copy.copy(listSnare)
    for x in range(steps):
        if len(playListKick)>0:
            if playListKick[0]==x:
                play_obj = KICK.play()
                MyMIDI.addNote(track, channel, 60, x, duration, velocity)
                playListKick.pop(0)
        if len(playListSnare)>0:
            if playListSnare[0]==x:
                play_obj = JACKU.play()
                MyMIDI.addNote(track, channel, 61, x, duration, velocity)
                playListSnare.pop(0)
        if len(playListMisc)>0:
            if playListMisc[0]==x:
                play_obj = BLIEP.play()
                MyMIDI.addNote(track, channel, 62, x, duration, velocity)
                playListMisc.pop(0)
        time.sleep(0.125)


print(listKick)
print(listSnare)
print(listMisc)
for x in range(repetitions):
    playSequence()

print("want to save midifile?")
print("0. no")
print("1. yes")
midiYoN=input("-> ")
while midiYoN.isdigit() == False:
    print("Please input integer.")
    midiYoN=input("-> ")
midiYoN=int(midiYoN)
while midiYoN > 1:
    print("Please input integer in range.")
    midiYoN=int(input("-> "))
if midiYoN == 1:
    with open("beeeaaat.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

