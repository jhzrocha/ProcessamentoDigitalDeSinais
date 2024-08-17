import numpy as np
import matplotlib.pyplot as plt

tamanho = 1000
sample_rate = 16000
frequenciaSenoide = 100
frequenciaAmostragem = 8000
duracao = 1
amplitude = 10000

write_path = "Aula 2/Audios/senoidal.pcm" 

t = np.arange(0, duracao*2, 1/frequenciaAmostragem)

senoide = np.sin(2 * np.pi * frequenciaSenoide * t) * amplitude

for i in range(0,len(senoide)):
    altura = senoide[i]
    plt.vlines(i, 0, altura, colors='blue')
    plt.scatter(i, altura, s=50, marker='o', color='blue')

senoide_int16 = np.int16(senoide)

with open(write_path, 'wb') as out_f:
    out_f.write(senoide_int16.tobytes())

plt.plot(t, senoide, label="Sinal Senoidal")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
