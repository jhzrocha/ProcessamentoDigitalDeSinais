import numpy as np
import matplotlib.pyplot as plt

tamanhoVetor = 36
posicaoImpulsoUnitario = 0
vetorEntrada = np.zeros(tamanhoVetor)

vetorEntrada[posicaoImpulsoUnitario] = 1

vetorResultado = np.copy(vetorEntrada)

n = 8
a0 = 0.9

# Loop de processamento
for j in range(0,tamanhoVetor):
    if(j - n >= 0):
        vetorResultado[j] = vetorResultado[j] + (a0 * vetorResultado[j-n])


# Plotando os resultados
plt.subplot(2,1,1).set_title('Vetor de Entrada')
plt.stem(np.arange(0, tamanhoVetor), vetorEntrada,'b', label='Função')

plt.subplot(2,1,2).set_title('Vetor de Saída - Delay  de 8')
plt.stem(np.arange(0, tamanhoVetor), vetorResultado,'b', label='Função')
plt.xlabel('n')

plt.show()
