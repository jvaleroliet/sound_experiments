from pyo import *
s = Server(duplex=1, nchnls=1).boot()
s.start()


# 1. Input environmental sounds
# inp = SfPlayer(input_file, loop=True)

snd = SndTable(r"C:\Users\juan\Documents\3. Other\Experimental Soudns\sound_experiments\field_recording_village.wav")

env = HannTable()
pos = Phasor(freq=snd.getRate(), mul=snd.getSize())
dur = Noise(mul=.001, add=.1)
g = Granulator(snd, env, 1, pos, dur, 24, mul=.1).out()



s.stop()