import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

frequenciaCorte = 200
frequenciaAmostragem = 8000

K = np.tan((np.pi*frequenciaCorte)/frequenciaAmostragem)
b0 = 1/(1+np.sqrt(2)*K+K**2)
b1 = -2/(1+np.sqrt(2)*K+K**2)
b2 = b0
a0 = 1
a1 = 2*(K**2-1)/(1+np.sqrt(2)*K+K**2)
a2 = (1-np.sqrt(2)*K+K**2)/(1+np.sqrt(2)*K+K**2)
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


