import numpy as np
import matplotlib.pyplot as plt

def load_pcm(filename, dtype=np.float32):
    with open(filename, 'rb') as f:
        data = np.frombuffer(f.read(), dtype=dtype)
    return data

def lms_filter(x, d, mu, M):
    """
    Aplica o algoritmo LMS para identificação de sistema.
    
    Parâmetros:
    x: sinal de entrada (numpy array)
    d: sinal desejado (numpy array)
    mu: passo de adaptação
    M: tamanho do filtro FIR
    
    Retorna:
    e: vetor de erro ao longo do tempo
    y: saída estimada pelo filtro adaptativo
    w: coeficientes finais do filtro
    """
    N = len(x)
    w = np.zeros(M, dtype=np.float32)
    y = np.zeros(N, dtype=np.float32)
    e = np.zeros(N, dtype=np.float32)
    
    # Para cada amostra a partir de M, formar o vetor de entrada do filtro
    for n in range(M, N):
        x_vec = x[n-(M-1):n+1][::-1] if M > 1 else x[n:n+1] 
        # Vetor x_vec com as M amostras passadas (x[n], x[n-1], ..., x[n-M+1])
        
        y[n] = np.dot(w, x_vec)  # Saída estimada
        e[n] = d[n] - y[n]       # Erro
        w += 2 * mu * e[n] * x_vec  # Atualização dos pesos
    
    return e, y, w


# Carregar sinais (ajuste os nomes dos arquivos conforme sua localização)
x = load_pcm('M3 - Prova/ruido_branco.pcm')
d = load_pcm('M3 - Prova/dn_Q1.pcm')

# Parâmetros a testar
mu_values = [0.001, 0.01, 0.05, 0.1]   # Diferentes passos de adaptação
M_values = [4, 8, 16, 32]             # Diferentes tamanhos do filtro

# Execução do LMS e plot dos resultados
plt.figure(figsize=(12, 8))
for i, mu in enumerate(mu_values):
    for j, M in enumerate(M_values):
        e, y, w = lms_filter(x, d, mu, M)
        
        plt.subplot(len(mu_values), len(M_values), i*len(M_values)+j+1)
        plt.plot(e)
        plt.title(f'$\mu$={mu}, M={M}')
        plt.xlabel('Amostras')
        plt.ylabel('Erro')
        plt.grid(True)
plt.tight_layout()
plt.show()
