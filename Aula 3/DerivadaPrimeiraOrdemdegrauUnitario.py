import numpy as np
import matplotlib.pyplot as plt

altura = 1000
tamanho = 10
inicioDegrauUnitario = 3

write_path = "Aula 3/Audios/MMDegrauUnitario.pcm"  

#Geração de Degrau Unitário
degrauUnitario = np.zeros(tamanho)

for i in range(inicioDegrauUnitario,len(degrauUnitario)):
    degrauUnitario[i] = altura

#Definição da Função usada no cálculo
funcao = degrauUnitario

#Cálculo da Derivada
t = np.arange(0,tamanho,1)
derivada = np.zeros_like(funcao)

for i in range(0,len(funcao)):
    derivada[i] = funcao[i] - funcao[i-1]

with open(write_path, 'wb') as out_f:
    out_f.write(derivada.tobytes())

plt.title("Derivada de Primeira Ordem")

plt.subplot(2,1,1).set_title('Função')
plt.stem(t,funcao,'r')

plt.subplot(2,1,2).set_title('Derivada de Primeira Ordem')
plt.stem(t,derivada,'b')

plt.xlim(0, tamanho)
plt.ylim(0, altura+100)

plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()



