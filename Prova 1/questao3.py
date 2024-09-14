import numpy as np
import matplotlib.pyplot as plt


read_path = 'Prova 1/Anexo_41743449.pcm'
write_path = 'Prova 1/SaidaQuestao3.pcm'
impulsoUnitário = np.zeros(10)
impulsoUnitário[0]=1
saidaImpulsoUnitario = []
# Definindo a entrada

with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    inputLen = len(data_i)
    vetorSaidaSeno = []
    
    yn1 = 0
    xn1 = 0

# Loop de processamento Impulso Unitario
    for j in range(0,len(impulsoUnitário)-1):         
        xn = impulsoUnitário[j]
        resultadoIteracao = xn - xn1 + 0.95*yn1
        yn1 = resultadoIteracao
        xn1 = xn        
        saidaImpulsoUnitario.append(resultadoIteracao)

    yn1 = 0
    xn1 = 0
    print(saidaImpulsoUnitario)
# Loop de processamento Audio
    for j in range(inputLen):
        xn = data_i[j]        
        resultadoIteracao = xn - xn1 + 0.95*yn1
        yn1 = resultadoIteracao
        xn1 = xn        
        vetorSaidaSeno.append(resultadoIteracao)
    
    vetorSaidaSeno16b = np.int16(vetorSaidaSeno)

    with open(write_path, 'wb') as out_f:
        out_f.write(vetorSaidaSeno16b.tobytes())

# Plotando os resultados
plt.stem(range(9), saidaImpulsoUnitario,'b', label='Função')
# plt.stem(saidaImpulsoUnitario, label='Entrada', linefmt='r-', markerfmt='ro', basefmt='r-', use_line_collection=True)
plt.title('Delay')
plt.legend()
plt.show()
