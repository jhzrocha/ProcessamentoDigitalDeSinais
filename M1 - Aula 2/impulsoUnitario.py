import numpy as np
import matplotlib.pyplot as plt

posicaoImpulsoUnitario = 400
altura = 1000
tamanho = 1000

write_path = "Aula 2/Audios/impulsoUnitario.pcm"

impulso = np.zeros(tamanho)
t = np.arange(0,tamanho,1)

impulso[posicaoImpulsoUnitario] = altura

with open(write_path, 'wb') as out_f:
    out_f.write(impulso.tobytes())

plt.title("Impulso Unitário")

plt.stem(t,impulso)

plt.xlim(0, len(impulso))
plt.ylim(0, altura + 100)

plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
