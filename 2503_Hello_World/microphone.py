from pyo import *                                                                                                                                                                                                                                                                                    
s = Server(duplex=1).boot()
s.start()
miccheck = Input().play().out()
miccheck.stop()