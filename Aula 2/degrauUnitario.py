import numpy as np
import matplotlib.pyplot as plt

altura = 1000
tamanho = 1000

write_path = "Aula 2/Audios/Degrau Unitário.pcm"  
impulso = np.zeros(tamanho)

with open(write_path, 'wb') as out_f:
    out_f.write(impulso.tobytes())

for i in range(0,tamanho):
    plt.vlines(i, 0, altura, colors='blue')
    plt.scatter(i, altura, s=50, marker='o', color='blue')

plt.xlim(0, tamanho)
plt.ylim(0, altura + 100)

plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
