import numpy as np
import matplotlib.pyplot as plt

posicaoImpulsoUnitario = 400
altura = 1000

write_path = "Aula 2/Audios/impulsoUnitario.pcm"  # Caminho para salvar o arquivo com ruído

# Criando o array do impulso unitário
impulso = np.zeros(10000)
impulso[posicaoImpulsoUnitario] = altura

# Salvando o impulso em um arquivo .pcm
with open(write_path, 'wb') as out_f:
    out_f.write(impulso.tobytes())

# Plotando apenas a reta do impulso unitário
plt.vlines(posicaoImpulsoUnitario, 0, altura, colors='blue', label="Impulso Unitário")

# Adicionando um círculo no ponto do impulso
plt.scatter(posicaoImpulsoUnitario, altura, s=50, marker='o')

# Ajustando os limites dos eixos para focar no impulso
plt.xlim(posicaoImpulsoUnitario - 10, posicaoImpulsoUnitario + 10)
plt.ylim(0, altura + 100)

plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
