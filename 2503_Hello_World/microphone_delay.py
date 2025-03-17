from pyo import *
s = Server(duplex=1, nchnls=1).boot()
s.start()
a = Input(chnl=0, mul=.7)
b = Delay(a, delay=.25, feedback=.5, mul=.5).out()


b.delay = 0.12
b.feedback = .8
s.stop()