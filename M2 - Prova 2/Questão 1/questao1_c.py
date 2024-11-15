import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

write_path = 'M2 - Prova 2/Questão 1/Saída.pcm' 
read_path = 'M2 - Prova 2/Questão 1/Anexo_42011575.pcm'
window_size = 20  # Defina o tamanho da janela de média móvel


with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    inputLen = len(data_i)
    mediaMovel = np.zeros(inputLen,dtype='float64')

    # Aplicação do filtro de média móvel
    for i in range(len(data_i)):
        for j in range(window_size):
            if (i - j >= 0):  # Certifique-se de que o índice não seja negativo
                mediaMovel[i] += (1 / window_size) * data_i[i - j]
    
    mediaMovel = mediaMovel.astype('int16')

    with open(write_path, 'wb') as out_f:
        out_f.write(mediaMovel.tobytes())
    
   
    t = np.arange(0, len(data_i), 1)
    plt.subplot(2,1,1).set_title('Função')
    plt.stem(t,data_i,'b', label='Função')
    plt.subplot(2,1,2).set_title('Média Móvel')
    plt.stem(t,mediaMovel,'g',label='Média Móvel')

    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()



