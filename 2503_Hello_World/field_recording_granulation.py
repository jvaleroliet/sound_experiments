from pyo import *
s = Server(duplex=1, nchnls=1).boot()
s.start()


# 1. Input environmental sounds
# inp = SfPlayer(input_file, loop=True)

mic = Input()

t = NewTable(length=5, chnls=1)
a = Input(0)
b = TableRec(a, t, .01)


env = HannTable()
pos = Phasor(freq=t.getRate(), mul=t.getSize())
dur = Noise(mul=.001, add=.1)
g = Granulator(t, env, [1, 1.001], 0, dur, 8, mul=.1).out()

# To record the granulator:
b.play()

s.stop()