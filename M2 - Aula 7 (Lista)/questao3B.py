import numpy as np
import matplotlib.pyplot as plt


degrauUnitario = [0,0,1,1,1,1,1,1,1,1,1]
resultado = []

for i in range(0,len(degrauUnitario)):
    x1 = 0
    x2 = 0
    x3 = 0
    if (i > 2):
        x3 = degrauUnitario[i-3]
    if (i > 1):
        x2 = degrauUnitario[i-2]
    if (i > 0):
        x1 = degrauUnitario[i-1]

    resultado.append(0.2*degrauUnitario[i] + 0.3*x1 + 0.3*x2 + 0.2*x3) 

t = np.arange(-2, len(degrauUnitario)-2, 1)
t2 = np.arange(-2, len(resultado)-2, 1)

plt.subplot(2,1,1).set_title('Degrau Unitário')
plt.stem(t, degrauUnitario[: len(t)],'b', label='Degrau Unitário')
plt.subplot(2,1,2).set_title('y(k) = 0.2x(k) + 0.3x(k-1) + 0.3x(k-2) + 0.2x(k-3)')
plt.stem(t2, resultado[: len(t2)],'b', label='y(k) = 0.2x(k) + 0.3x(k-1) + 0.3x(k-2) + 0.2x(k-3)')

plt.show()
