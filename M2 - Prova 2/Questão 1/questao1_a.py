import numpy as np
import matplotlib.pyplot as plt
from scipy import signal    

b = np.ones(8) / 8  # Coeficientes do numerador
a = [1]             # Coeficientes do denominador

# Calcular a resposta em frequência
w, h = signal.freqz(b, a)
    
plt.figure(figsize=(12, 6))
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.title('Resposta em Frequência do Filtro de Média Móvel (N=8)')
plt.xlabel('Frequência Normalizada [radianos / amostra]')
plt.ylabel('Magnitude [dB]')
plt.grid()
plt.show()

# Calcular e plotar polos e zeros
z, p, k = signal.tf2zpk(b, a)
plt.figure(figsize=(6, 6))
plt.scatter(np.real(z), np.imag(z), marker='o', color='b', label='Zeros')
plt.scatter(np.real(p), np.imag(p), marker='x', color='r', label='Polos')
plt.title('Diagrama de Polos e Zeros')
plt.xlabel('Real')
plt.ylabel('Imaginário')
plt.grid()
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.legend()
plt.axis('equal')
plt.show()