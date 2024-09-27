import numpy as np
import matplotlib.pyplot as plt

data_len = 1000
sample_rate = 16000


t = np.arange(0, data_len, 1)

x1 = np.sin(2 * np.pi * 400 * t / sample_rate)
x2 = np.sin(2 * np.pi * 1200 * t / sample_rate)

h = np.zeros(x1.size)
for x in range(len(h)):
    h[x] = x1[x] + x2[x]

resultado = []
for i in range(0,len(h)):    
    resultadoParcial = 0
    for m in range(0,len(h)):
        resultadoParcial = resultadoParcial + h[m]*np.exp(-1j*(np.pi/len(h))*m*i)
    resultado.append(abs(resultadoParcial))

t2 = np.arange(0, len(resultado)/2, 1)


plt.subplot(2,1,1).set_title('Onda de Entrada')
plt.stem(t, h[: len(t)],'b', label='Função')
plt.subplot(2,1,2).set_title('Frequencia')
plt.stem(t2*8, resultado[: len(t2)],'b', label='Função')

plt.show()
