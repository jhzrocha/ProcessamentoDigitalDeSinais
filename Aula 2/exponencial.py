import numpy as np
import matplotlib.pyplot as plt

frequenciaAmostragem = 1 #em Hertz
duracao = 5 #em Segundos
amplitude = 1
listaTaxaCrescimento = [0.5,-0.5,2]
for taxa_crescimento in listaTaxaCrescimento:
    write_path = f"Aula 2/Audios/exponencial_{taxa_crescimento}.pcm" 

    t = np.arange(0, duracao, 1/frequenciaAmostragem)
    exponencial = amplitude * np.power(taxa_crescimento, t)
    exponencial_int16 = np.int16(exponencial / np.max(exponencial) * 32767) 

    with open(write_path, 'wb') as out_f:
        out_f.write(exponencial_int16.tobytes())

    totalEnergia = np.sum(exponencial ** 2)

    plt.stem(t, exponencial)
    
    plt.title(f"Taxa de Crescimento: {taxa_crescimento}")
    plt.text(0.5, 0.9, f"Total de Energia: {totalEnergia:.2f}",
         transform=plt.gca().transAxes,
         fontsize=12, verticalalignment='top')
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()
