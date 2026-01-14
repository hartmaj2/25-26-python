# 1. Plays frequencies for given durations
# 2. Recovers relative indices of notes from A_4 from the frequencies in the list

import numpy as np
import sounddevice as sd

import math

frequencies = [659, 587, 523, 587, 659, 659, 659, 587, 587, 587, 659, 783, 783]

durations = [1,1,1,1,1,1,2,1,1,2,1,1,2]

def play_tone(freq, duration=1.0, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * freq * t)
    sd.play(signal, sample_rate)
    sd.wait()

def freq(n : int) -> float:
    return 440 * (2**(n/12))

for f,d in zip(frequencies,durations):
    play_tone(f,d/5)

notes = [round(12 * math.log(f/440,2)) for f in frequencies]
print(notes)
