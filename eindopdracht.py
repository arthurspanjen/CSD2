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

#make user select timesignature. Makes sure they have to pick either the integer 1 or integer 2.
print("Select time signature:")
print("1. 5/4")
print("2. 6/8")
correctTimeSignature=0
timeSignature=input("-> ")
while correctTimeSignature==0:
    if timeSignature.isdigit()==False:
        print("Please input integer")
        timeSignature=input("-> ")
    elif int(timeSignature) > 2:
        print("Please input integer in range")
        timeSignature=input("-> ")
    elif int(timeSignature) < 1:
        print("Please input integer in range")
        timeSignature=input("-> ")
    else:
        correctTimeSignature=1

#set all parameters that change with different time signatures
timeSignature=int(timeSignature)
if timeSignature==1:
    steps=20
    numerator=5
    denominator=2
    metronome=24
if timeSignature==2:
    steps=12    
    numerator=6
    denominator=3
    metronome=12

#set bpm. makes sure user picks a number between 60 and 199.
correctBpm=0
print("Bpm?")
bpm=input("-> ")
while correctBpm==0:
    if bpm.isdigit()==False:
        print("Please input integer.")
        bpm=input("-> ")
    elif int(bpm)<60:
        print("Please choose a bpm higher than 59.")
        bpm=input("-> ")
    elif int(bpm)>200:
        print("Please choose a bpm lower than 200.")
        bpm=input("-> ")
    else:
        correctBpm=1
bpm=int(bpm)
velocity=100


#initialize midifile
track=0
channel=9
Mtime=0
duration=0.25
MyMIDI = MIDIFile(2)
MyMIDI.addTempo(track,Mtime,bpm)
sleepTime=60/(bpm*4)

#set how many times the beat should be played
print("how many repititions?")
repetitions=input("-> ")
while repetitions.isdigit() == False:
    print("Please input integer.")
    repetitions=input("-> ")
repetitions=int(repetitions)

#make three empty lists for Kick, Snare and Misc sound
listKick=[]
listSnare=[]
listMisc=[]

#initialize Placed numbers, makes sure there is no snare on the first beat.
kickPlaced=0
snarePlaced=1
miscPlaced=0

#makes the list for every sound, makes sure there is a kick on the first beat and a clap on the second.
#Kick and snare are on a grid of eight notes, misc is on a grid of sixteenth notes.
#there is at least one eight between each kick and snare, and at least one sixteenth between every misc. 
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
    
#making midifile and copying lists for playback.
MyMIDI.addTimeSignature(track, 0, numerator, denominator, metronome)
playListMisc=copy.copy(listMisc)
playListKick=copy.copy(listKick)
playListSnare=copy.copy(listSnare)

#plays back every list using the pop() function and a for loop. Writes midi file simeltaneously
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
        time.sleep(sleepTime)


print(listKick)
print(listSnare)
print(listMisc)

#makes sure it loops for as many times as the user input
for x in range(repetitions):
    playSequence()

#ask the user if (s)he wants to save the midifile. Can only input integers 0 & 1
print("want to save midifile?")
print("0. no")
print("1. yes")
correctMidiYoN=0
midiYoN=input("-> ")
while correctMidiYoN==0:
    if midiYoN.isdigit() == False:
        print("Please input integer.")
        midiYoN=input("-> ")
    elif int(midiYoN) > 1:
        print("Please input integer in range.")
        midiYoN=input("-> ")
    elif int(midiYoN) < 0:
        print("please input integer in range.")
        midiYoN=input("-> ")
    else: 
        correctMidiYoN=1


#if user choose to make midifile, gets written to harddisk
midiYoN=int(midiYoN)
if midiYoN == 1:
    print("Name midi:")
    midiName=input("-> ")
    with open(midiName+".mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

