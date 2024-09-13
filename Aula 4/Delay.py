import numpy as np
import matplotlib.pyplot as plt


read_path = 'Aula 4/Audios/delay.pcm'
write_path = "Aula 4/Audios/SaídaDelay.pcm"  

# Parâmetros
Fs = 16000
t1 = 40 * 10**-2
t2 = 80 * 10**-2

n1 = int(t1 * Fs)
n2 = int(t2 * Fs)

# Definição dos ganhos
a0 = 0.5
a1 = 0.3
a2 = 0.2

tama_delay = n2

# Definindo a entrada

with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    inputLen = len(data_i)
    vetorDelays = np.zeros(inputLen)

# Loop de processamento
    for j in range(inputLen):
        input_signal = data_i[j]            
        vetorDelays[j]= (a0 * data_i[j] + a1 * data_i[j - n1] + a2 * data_i[j - n2])*2
    delays16b = np.int16(vetorDelays)

    with open(write_path, 'wb') as out_f:
        out_f.write(delays16b.tobytes())

# Plotando os resultados
    plt.stem(data_i, label='Saída', linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.stem(vetorDelays, label='Entrada', linefmt='r-', markerfmt='ro', basefmt='r-', use_line_collection=True)
    plt.title('Delay')
    plt.legend()
    plt.show()
