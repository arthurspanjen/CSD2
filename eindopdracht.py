import simpleaudio as sa
import time
import datetime
from random import randint
import copy
from multiprocessing import Process
import sys

KICK = sa.WaveObject.from_wave_file("808kick.wav")
BLIEP = sa.WaveObject.from_wave_file("808cow.wav")
JACKU = sa.WaveObject.from_wave_file("808clap.wav")

startTime=int(time.time())

print("how many repititions?")
repetitions=int(input("-> "))

listKick=[]
listSnare=[]
listMisc=[]

kickPlaced=0
snarePlaced=1
miscPlaced=0

steps=20
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
        if x == 5:
            listSnare.append(x)
            snarePlaced=1
        if x !=  5:
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
                playListKick.pop(0)
        if len(playListSnare)>0:
            if playListSnare[0]==x:
                play_obj = JACKU.play()
                playListSnare.pop(0)
        if len(playListMisc)>0:
            if playListMisc[0]==x:
                play_obj = BLIEP.play()
                playListMisc.pop(0)
        time.sleep(0.125)

userYoN=1
while userYoN==1:
    print(listKick)
    print(listSnare)
    print(listMisc)
    for x in range(repetitions):
        playSequence()
    print("again??")
    userYoN=int(input("-> "))
    if userYoN==1:
        print("how many repetitions?")
        repetitions=int(input("-> "))
