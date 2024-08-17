import numpy as np
import matplotlib.pyplot as plt

altura = 1000
tamanho = 10

write_path = "Aula 2/Audios/Degrau Unitário.pcm"  

degrauUnitario = np.zeros(tamanho)
t = np.arange(0,tamanho,1)

for i in range(0,len(degrauUnitario)):
    degrauUnitario[i] = altura

with open(write_path, 'wb') as out_f:
    out_f.write(degrauUnitario.tobytes())

plt.title("Degrau Unitário")
plt.stem(t,degrauUnitario)
plt.xlim(0, tamanho)
plt.ylim(0, altura+100)

plt.legend()
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.show()
