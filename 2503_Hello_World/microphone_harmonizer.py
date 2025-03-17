from pyo import *
s = Server(duplex=1, nchnls=1).boot()
s.start()


mic = Input().play().out()


env = WinTable(8)
wsize = .1
trans = -7

ratio = pow(2., trans/12.)
rate = -(ratio-1) / wsize

ind = Phasor(freq=rate, phase=[0,0.5])
win = Pointer(table=env, index=ind, mul=.7)
snd = Delay(mic, delay=ind*wsize, mul=win).mix(1).out(1)


s.stop()