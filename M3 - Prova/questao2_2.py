import numpy as np
import matplotlib.pyplot as plt

def load_pcm(filename, dtype=np.float32):
    """Carregar arquivo PCM."""
    with open(filename, 'rb') as f:
        data = np.frombuffer(f.read(), dtype=dtype)
    return data

def lms_algorithm(x, d, u, M):
    """
    Implementação do algoritmo LMS.
    
    x: Sinal de entrada.
    d: Sinal desejado.
    u: Passo de adaptação.
    M: Tamanho do filtro adaptativo.
    """
    N = len(x)
    w = np.zeros(M)  # Inicialização dos coeficientes do filtro
    e = np.zeros(N)  # Erro
    y = np.zeros(N)  # Saída do filtro
    
    for n in range(M, N):
        # Vetor de entrada (janelas do sinal de entrada)
        x_n = x[n:n-M:-1]
        # Saída do filtro
        y[n] = np.dot(w, x_n)
        # Erro
        e[n] = d[n] - y[n]
        # Atualização dos coeficientes do filtro
        w += 2 * u * e[n] * x_n
    
    return e, y, w

# Carregar os sinais x[n] e d[n]
x = load_pcm('M3 - Prova/ruido_branco.pcm', dtype=np.float32)
d = load_pcm('M3 - Prova/dn_Q2.pcm', dtype=np.float32)

# Parâmetros do LMS
M_values = [4, 8, 16]  # Diferentes tamanhos do filtro adaptativo
u_values = [0.01, 0.05, 0.1]  # Diferentes passos de adaptação

plt.figure(figsize=(12, 8))

# Iterar sobre diferentes valores de M e u
for i, M in enumerate(M_values):
    for j, u in enumerate(u_values):
        e, y, w = lms_algorithm(x, d, u, M)
        plt.subplot(len(M_values), len(u_values), i * len(u_values) + j + 1)
        plt.plot(e, label=f'u={u}, M={M}')
        plt.title(f'Erro (u={u}, M={M})')
        plt.xlabel('Amostras')
        plt.ylabel('Erro (e[n])')
        plt.grid(True)
        plt.legend()

plt.tight_layout()
plt.show()
