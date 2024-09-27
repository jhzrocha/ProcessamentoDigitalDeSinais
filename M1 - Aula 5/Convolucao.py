import numpy as np
import matplotlib.pyplot as plt

degrauUnitario = np.array([1, 1, 1, 1, 1, 1])
vetor = np.array([1, 0.5, 0.25, 0.125])
impulsoUnitário = np.array([0,0,0,1, 0, 0, 0, 0, 0])

convDegrauUnitarioEVetor = np.convolve(degrauUnitario, vetor)
convImpulsoUnitarioEVetor = np.convolve(impulsoUnitário, vetor)

tama = len(degrauUnitario) + len(vetor) - 1
tamb = len(impulsoUnitário) + len(vetor) - 1
n1 = np.arange(0, tama)
n2 = np.arange(0, tamb)

plt.subplot(2,1,1).set_title('Convolução de degrauUnitario e vetor')
plt.stem(n1, convDegrauUnitarioEVetor,'b', label='Função')

plt.subplot(2,1,2).set_title('Convolução de Impulso Unitário e vetor')
plt.stem(n2, convImpulsoUnitarioEVetor,'b', label='Função')
plt.xlabel('n')

plt.show()
