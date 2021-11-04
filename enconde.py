#!/usr/bin/env python3
"""Show a text-mode spectrogram using live microphone data."""

#Importe todas as bibliotecas
import numpy as np
from numpy.lib.nanfunctions import nancumprod
import sounddevice as sd
import matplotlib as plt
import peakutils 
#from suaBibSignal import *
import time 
import soundfile as sf

audio, samplerate = sf.read('audio/ac130.wav')
print(samplerate)