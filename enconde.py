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
from suaBibSignal import *

audio, samplerate = sf.read('audio/ac130.wav')
print(samplerate)

audio = audio*10e5

freqDeAmostragem = 44100
duracao = 2
numAmostras = freqDeAmostragem*duracao


inicio = 0
fim = 2
numPontos = numAmostras

t = np.linspace(inicio,fim,numPontos)
# plot do gravico  áudio vs tempo!
plt.plot(t, audio[:88200,0])

signal= signalMeu()
fs = freqDeAmostragem
xf, yf = signal.calcFFT(audio[:,0], fs)
plt.figure("F(y)")
plt.plot(xf,yf)
plt.grid()
plt.title('Fourier audio')