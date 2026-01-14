# Plays random tones from major scale for random durations

import numpy as np
import sounddevice as sd

import random

def play_tone(freq, duration=1.0, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * freq * t)
    sd.play(signal, sample_rate)
    sd.wait()

def f(n : int) -> float:
    return 440 * (2**(n/12))

tones = [440 * (2**(i/12)) for i in range(-10,13)]

major_scale = [0,2,4,5,7,9,11,12]
durations = [0.1 * (2**i) for i in range(-3,5)]

for i in range(100):
    j = random.choice(major_scale)
    t = random.choice(durations)
    play_tone(tones[j],t)


# for i in major:
#     play_tone(tones[i],0.1)

# play_tone(440, 1.5)  # A4 = 440 Hz