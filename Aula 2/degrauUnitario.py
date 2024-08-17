import numpy as np
import matplotlib.pyplot as plt

altura = 1000
tamanho = 10

write_path = "Aula 2/Audios/Degrau Unitário.pcm"  

impulso = np.zeros(tamanho)
t = np.arange(0,tamanho,1)

for i in range(0,len(impulso)):
    impulso[i] = altura

with open(write_path, 'wb') as out_f:
    out_f.write(impulso.tobytes())

plt.title("Degrau Unitário")
plt.stem(t,impulso)
plt.xlim(0, tamanho)
plt.ylim(0, altura+100)

plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
