import numpy as np
import matplotlib.pyplot as plt

altura = 1000
tamanho = 1000
sample_rate = 16000
frequenciaSenoide = 100
taxa_crescimento = 1
frequenciaAmostragem = 8000
duracao = 1
amplitude = 10000

write_path = "Aula 2/Audios/exponencial.pcm" 

t = np.arange(0, duracao*2, 1/frequenciaAmostragem)

exponencial = amplitude * np.exp(taxa_crescimento * t)

exponencial_int16 = np.int16(exponencial / np.max(exponencial) * 32767) 

with open(write_path, 'wb') as out_f:
    out_f.write(exponencial_int16.tobytes())

plt.plot(t, exponencial, label="Sinal Exponencial")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
