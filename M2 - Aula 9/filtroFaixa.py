import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

frequenciaCorte = 1000
frequenciaAmostragem = 8000
frequenciaBanda = 200

c = np.tan(np.pi*frequenciaBanda/frequenciaCorte)-1/(np.tan(2*np.pi*frequenciaBanda/frequenciaCorte)-1)
d = -np.cos(2*np.pi*(frequenciaCorte/frequenciaAmostragem))

b0 = 0.5*(1+c)
b1 = 0
b2 = (-c-1)/2
a0 = 1
a1 = d*(1-c)
a2 = -c
den_ = [1,a1, a2]
num_ = [b0,b1,b2]

[w, h] = freqz(num_, den_, worN=frequenciaAmostragem, fs=frequenciaAmostragem)

zero = np.roots(num_)
polo1 = np.roots(den_)
plt.figure(figsize=(6, 6))
circulo = plt.Circle((0, 0), 1, color='blue', fill=False, linestyle='--', label='Círculo Unitário')
plt.gca().add_artist(circulo)

plt.scatter(np.real(zero), np.imag(zero), color='green', label='Zeros', s=100)
plt.scatter(np.real(polo1), np.imag(polo1), color='red', label='Polos', s=100)

plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Polos e Zeros no Plano Complexo z')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
plt.axis([0,3600,-30,1])
plt.plot(w, 20*np.log10(abs(h)), 'b')
plt.show()


