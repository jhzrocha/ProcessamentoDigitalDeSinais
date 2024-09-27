import numpy as np
import matplotlib.pyplot as plt


read_path = 'M2 - Aula 6/Audios/RuidoBranco.pcm'
with open(read_path, 'rb') as f:
    buf = f.read()
    h = np.frombuffer(buf, dtype='int16')
    t = np.arange(0, len(h), 1)

    resultado = []
    for i in range(0,len(h)):    
        resultadoParcial = 0
        for m in range(0,len(h)):
            resultadoParcial = resultadoParcial + h[m]*np.exp(-1j*(np.pi/len(h))*m*i)
        resultado.append(abs(resultadoParcial))

    t2 = np.arange(0, len(resultado)/2, 1)

    plt.subplot(2,1,1).set_title('Onda de Entrada')
    plt.stem(t, h[: len(t)],'b', label='Função')
    plt.subplot(2,1,2).set_title('Frequencia')
    plt.stem(t2*8, resultado[: len(t2)],'b', label='Função')

    plt.show()
