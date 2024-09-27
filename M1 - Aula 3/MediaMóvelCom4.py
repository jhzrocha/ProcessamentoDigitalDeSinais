import numpy as np
import matplotlib.pyplot as plt

frequenciaSenoide = 10
frequenciaAmostragem = 100
duracao = 2
amplitude = 10000
write_path = "Aula 3/Audios/MediaMovelCom4.pcm"  

altura = 1000
tamanho = 10
inicioDegrauUnitario = 3

#Gera a função de Degrau Unitário
degrauUnitario = np.zeros(tamanho)
for i in range(inicioDegrauUnitario,len(degrauUnitario)):
    degrauUnitario[i] = altura

#Início do Cálculo de Média Móvel
funcao = degrauUnitario
t = np.arange(0, len(funcao), 1)
mediaMovel = np.zeros_like(funcao)

for i in range(0,len(funcao)):
    mediaMovel[i] = 0.25* funcao[i]
    #If para evitar consultas de index negativos, algo que pega o último valor do vetor em Python
    if (i-1 > 0):
        mediaMovel[i] = mediaMovel[i] + 0.25* funcao[i-1]
    if (i-2 > 0):
        mediaMovel[i] = mediaMovel[i] + 0.25* funcao[i-2]
    if (i-3 > 0):
        mediaMovel[i] = mediaMovel[i] + 0.25* funcao[i-3]

#Escrita do arquivo
with open(write_path, 'wb') as out_f:
    out_f.write(mediaMovel.tobytes())

plt.subplot(2,1,1).set_title('Função')
plt.stem(t,funcao,'b', label='Função')
plt.subplot(2,1,2).set_title('Média Móvel')
plt.stem(t,mediaMovel,'g',label='Média Móvel')

plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()



