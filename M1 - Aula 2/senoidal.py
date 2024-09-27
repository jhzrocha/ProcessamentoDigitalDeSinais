import numpy as np
import matplotlib.pyplot as plt

frequenciaSenoide = 100
frequenciaAmostragem = 2000
duracao = 1
amplitude = 10000

write_path = "Aula 2/Audios/senoidal.pcm" 

t = np.arange(0, duracao, 1/frequenciaAmostragem)

senoide = np.cos(2 * np.pi * frequenciaSenoide * t) * amplitude

senoide_int16 = np.int16(senoide)

with open(write_path, 'wb') as out_f:
    out_f.write(senoide_int16.tobytes())

plt.title("Senoidal")
plt.stem(t, senoide)
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
