import numpy as np
import matplotlib.pyplot as plt


degrauUnitario = [0,0,1,1,1,1,1,1,1,1,1]
resultado = []

for i in range(0,len(degrauUnitario)):
    y1 = 0
    y2 = 0

    if (len(resultado) > 1):
        y1 = resultado[-1]
    if (len(resultado) > 2):
        y2 = resultado[-2]

    resultado.append(degrauUnitario[i] + 0.25*y1 - 0.5*y2) 

t = np.arange(-2, len(degrauUnitario)-2, 1)
t2 = np.arange(-2, len(resultado)-2, 1)

plt.subplot(2,1,1).set_title('Degrau Unitário')
plt.stem(t, degrauUnitario[: len(t)],'b', label='Degrau Unitário')
plt.subplot(2,1,2).set_title('y(k) = x(k) + 1/4y(k-1) - 1/2y(k-2)')
plt.stem(t2, resultado[: len(t2)],'b', label='y(k) = x(k) + 1/4y(k-1) - 1/2y(k-2)')

plt.show()
