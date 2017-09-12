data = int(input ("hoeveel? "))
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("bwaah.wav")

for i in range(data):
	play_obj = wave_obj.play()
	play_obj.wait_done()
