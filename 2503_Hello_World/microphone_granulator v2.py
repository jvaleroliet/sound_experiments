from pyo import *
s = Server(duplex=1, nchnls=1).boot()
s.start()


# 1. Input environmental sounds
# inp = SfPlayer(input_file, loop=True)


env = HannTable()
pos = Phasor(freq=snd.getRate(), mul=snd.getSize())
dur = Noise(mul=.001, add=.1)
g = Granulator(snd, env, 1, pos, dur, 24, mul=.1).out()

input_file = r"C:\Users\juan\Documents\3. Other\Experimental Soudns\sound_experiments\field_recording_village.wav"

# 1. Input environmental sounds
inp = SfPlayer(input_file, loop=True)

# 2. Simulate gate generation (Simplified peak detection)
env = Follower(inp, mul=0.5)  # Follow the amplitude
threshold = 0.2  # Adjust threshold as needed
gate = Compare(env, threshold, ">")  # Create a gate based on threshold

# 3. Simulate ping filter and Rings-like synthesis
# Ping Filter simulation (Simple resonant filter with gate-triggered excitation)
freq = Sig(220)  # Base frequency
res = Sig(0.8)  # Resonance
ping_filter = Biquad(gate * 0.5, freq=freq, q=res, type=2) # type 2 is bandpass

# Rings-like simulation (Using a modulated oscillator)
fundamental = Sig(110)
mod_freq = LFO(freq=0.5, type=2, mul=10, add=fundamental) # low frequency oscillator to modulate the pitch
ring_osc = Osc(table=HarmTable([1, 0.5, 0.25]), freq=mod_freq, mul=0.2) #Harmtable to create rich tones

# Combine ping filter and Rings-like sounds
combined_osc = ping_filter + ring_osc

# 4. Simulate Morphagene and Mimeophon-like effects
# Morphagene-like simulation (Using a combination of delay and pitch shifting)
delay_time = Sig(0.1) # grain size in seconds
pitch_shift = Sig(1.01) # slight pitch shift for granular effect
morph_effect = Delay(combined_osc, delay=delay_time, feedback=0.3) * FreqShift(combined_osc, shift=pitch_shift, mul=0.3)

# Mimeophon-like simulation (Multi-tap delay)
delay_time2 = Sig(0.25)
feedback = Sig(0.6)
mimeo_effect = Delay(morph_effect, delay=delay_time2, feedback=feedback, mul=0.7)

# Final output
final_output = inp  + mimeo_effect

final_output.out()
s.stop()