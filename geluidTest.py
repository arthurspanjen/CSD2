import simpleaudio as sa
import time

print("kies soundpack: ")
print("1. 808")
print("2. lofi")
print("3. trap")


sp = input("-> ")
while sp.isdigit() == False:
    print("NEE!!!")
    sp=input("-> ")
sp=int(sp)

if sp == 1:
    KICK = sa.WaveObject.from_wave_file("808kick.wav")
    BLIEP = sa.WaveObject.from_wave_file("808cow.wav")
    JACKU = sa.WaveObject.from_wave_file("808clap.wav")
elif sp == 2:
    KICK = sa.WaveObject.from_wave_file("lofiKick.wav")
    BLIEP = sa.WaveObject.from_wave_file("lofiMisc.wav")
    JACKU = sa.WaveObject.from_wave_file("lofiSnare.wav")
elif sp == 3:
    KICK = sa.WaveObject.from_wave_file("trapKick.wav")
    BLIEP = sa.WaveObject.from_wave_file("trapMisc.wav")
    JACKU = sa.WaveObject.from_wave_file("jacku.wav")

tempo= int(input("tempo -> "))
tempo= float((60/tempo) * 0.5)
print(tempo)
kick = input("kicklijst---> ")
l1 = list(map(int, kick.split()))
bliep = input("misclijst---> ")
l2 = list(map(int, bliep.split()))
jacku = input("snarelijst--> ")
l3 = list(map(int, jacku.split()))

x=0
y=0
while (x < 1):
    y=y%8
    if (y==0):
        if l1[-8] == 1:
            play_obj_kick = KICK.play()
        if l2[-8] == 1:
            play_obj_kick = BLIEP.play()
        if l3[-8] == 1:
            play_obj_kick = JACKU.play()

    elif (y==1):
        if l1[-7]== 1:
            play_obj_kick = KICK.play()
        if l2[-7] == 1:
            play_obj_kick = BLIEP.play()
        if l3[-7] == 1:
            play_obj_kick = JACKU.play()

    elif (y==2):
        if l1[-6] == 1:
            play_obj_kick = KICK.play()
        if l2[-6] == 1:
            play_obj_kick = BLIEP.play()
        if l3[-6] == 1:
            play_obj_kick = JACKU.play()

    elif (y==3):
        if l1[-5] == 1:
            play_obj_kick = KICK.play()
        if l2[-5] == 1:
            play_obj_kick = BLIEP.play()
        if l3[-5] == 1:
            play_obj_kick = JACKU.play()

    elif (y==4):
        if l1[-4] == 1:
            play_obj_kick = KICK.play()
        if l2[-4] == 1:
            play_obj_kick = BLIEP.play()
        if l3[-4] == 1:
            play_obj_kick = JACKU.play()
   
    elif (y==5):
        if l1[-3] == 1:
            play_obj_kick = KICK.play()
        if l2[-3] == 1:
            play_obj_kick = BLIEP.play()
        if l3[-3] == 1:
            play_obj_kick = JACKU.play()

    elif (y==6):
        if l1[-2] == 1:
            play_obj_kick = KICK.play()
        if l2[-2] == 1:
            play_obj_kick = BLIEP.play()
        if l3[-2] == 1:
            play_obj_kick = JACKU.play()

    elif (y==7):
        if l1[-1] == 1:
            play_obj_kick = KICK.play()
        if l2[-1] == 1:
            play_obj_kick = BLIEP.play()
        if l3[-1] == 1:
            play_obj_kick = JACKU.play()
    time.sleep(tempo)	
    y=y+1


#play_obj_bliep = BLIEP.play()
#play_obj_bliep.wait_done()


#play_obj_kick = KICK.play()
#play_obj_kick.wait_done()


#play_obj_jacku = JACKU.play()
#play_obj_jacku.wait_done()
