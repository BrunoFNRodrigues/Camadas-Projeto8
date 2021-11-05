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
from funcoes_LPF import *

audio, samplerate = sf.read('audio/ac130.wav')
print(samplerate)

audio = audio*(1/0.15)

freqDeAmostragem = 44100
duracao = 2
numAmostras = freqDeAmostragem*duracao


inicio = 0
fim = 2
numPontos = numAmostras

t = np.linspace(inicio,fim,numPontos)
# plot do gravico  áudio vs tempo!
plt.title('Audio puro')
plt.plot(t, audio[:88200,0])


signal= signalMeu()
fs = freqDeAmostragem
xf, yf = signal.calcFFT(audio[:,0], fs)
plt.figure("F(y)")
plt.plot(xf,yf)
plt.grid()
plt.title('Fourier audio')
plt.show()


filtrado = filtro(audio[:88200,0], samplerate, 14000)
#sd.play(filtrado, samplerate)

t = np.linspace(inicio,fim,numPontos)
# plot do gravico  áudio vs tempo!
plt.plot(t, filtrado)
plt.title('Audio filtrado')
plt.show()


xf, yf = signal.calcFFT(filtrado, fs)
plt.figure("F(y)")
plt.plot(xf,yf)
plt.grid()
plt.title('Fourier audio filtrado')
plt.show()


y, x = signal.generateSin(14000, 1, duracao, freqDeAmostragem)

X=x+filtrado*x
#sd.play(X)


plt.plot(t, X)
plt.title('Audio modulado')
plt.show()


xf, yf = signal.calcFFT(X, fs)
plt.figure("F(y)")
plt.plot(xf,yf)
plt.grid()
plt.title('Fourier audio modulado')
plt.show()

sf.write('teste.wav', X, samplerate)


