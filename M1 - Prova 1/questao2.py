import numpy as np
import matplotlib.pyplot as plt

tamanhoVetorResultado = 9
degrauUnitario = np.ones(tamanhoVetorResultado)
degrauUnitarioMenos2 = np.ones(tamanhoVetorResultado)
x = np.zeros(tamanhoVetorResultado)

h = np.array([0.1,0.2,0.4,0.2,0.1])
impulsoUnitário = np.zeros(tamanhoVetorResultado)
impulsoUnitário[0] = 1

#Desloca o degrau unitário 2 unidades para a direita
for i in range(0,len(degrauUnitarioMenos2)):
    if (i < 2):
        degrauUnitarioMenos2[i] = 0


#Realiza a subtração dos degrais unitários
for j in range(0,len(x)):
    x[j] = degrauUnitario[j]-degrauUnitarioMenos2[j]


convDegrauUnitarioEH = np.convolve(x, h)
convImpulsoUnitarioEH = np.convolve(impulsoUnitário, h)

tama = len(degrauUnitario) + len(h) - 1
tamb = len(impulsoUnitário) + len(h) - 1
n1 = np.arange(0, tama)
n2 = np.arange(0, tamb)

plt.subplot(2,1,1).set_title('Convolução de degrauUnitario e vetor')
plt.stem(range(9), convDegrauUnitarioEH[0:9],'b', label='Função')

plt.subplot(2,1,2).set_title('Convolução de Impulso Unitário e vetor')
plt.stem(range(9), convImpulsoUnitarioEH[0:9],'b', label='Função')
plt.xlabel('n')

plt.show()

