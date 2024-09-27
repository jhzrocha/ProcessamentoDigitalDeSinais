import numpy as np
import matplotlib.pyplot as plt

gain = 0.5
sample_rate = 16000

read_path = "teste.pcm" # Orig ../teste.pcm
write_path = "teste_com_barulho.pcm"  # Caminho para salvar o arquivo com ruído

with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)
    data_o = np.zeros_like(data_i)

    t = np.arange(0, data_len, 1)
    ruido = np.sin(2 * np.pi * 400 * t / sample_rate) * 1000
    
    data_o = np.clip(data_o, np.iinfo(np.int16).min, np.iinfo(np.int16).max)

    for i in range(data_len):
        data_o[i] = data_i[i] + ruido[i]

    with open(write_path, 'wb') as out_f:
        out_f.write(data_o.tobytes())

    plt.plot(t, data_i[: len(t)], label="Input")
    plt.plot(t, data_o[: len(t)], label="Output com ruido")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()
