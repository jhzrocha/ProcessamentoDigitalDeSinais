import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

def load_pcm(filename, dtype=np.float32):
    """Carregar arquivo PCM."""
    with open(filename, 'rb') as f:
        data = np.frombuffer(f.read(), dtype=dtype)
    return data

def clean_signal(signal):
    """Corrigir valores inválidos (NaN ou infinito) no sinal."""
    signal = np.nan_to_num(signal, nan=0.0, posinf=0.0, neginf=0.0)  # Substituir NaN/Infinito por zero
    signal = np.clip(signal, -1e6, 1e6)  # Limitar valores extremos
    return signal

# Parâmetros do filtro
Fs = 8000.0  # Frequência de amostragem
Fc = 400.0   # Frequência de corte
f_norm = Fc / (Fs / 2.0)
order = 2

# Projeto do filtro
b, a = butter(order, f_norm, btype='high', analog=False)

# Carregar sinal de entrada
input_file = 'M3 - Prova/ruido_branco.pcm'
try:
    x = load_pcm(input_file, dtype=np.float32)
    print(f"Sinal carregado com sucesso. Número de amostras: {len(x)}")
except FileNotFoundError:
    print(f"Arquivo não encontrado: {input_file}")
    x = np.zeros(1000)  # Usar um sinal dummy para evitar erros

# Diagnóstico do sinal antes da limpeza
print(f"Primeiros 10 valores do sinal de entrada (original): {x[:10]}")
print(f"Valor máximo (original): {np.max(x)}")
print(f"Valor mínimo (original): {np.min(x)}")

# Limpar sinal
x = clean_signal(x)

# Diagnóstico do sinal após a limpeza
print(f"Primeiros 10 valores do sinal de entrada (limpo): {x[:10]}")
print(f"Valor máximo (limpo): {np.max(x)}")
print(f"Valor mínimo (limpo): {np.min(x)}")

# Aplicar o filtro
y = filtfilt(b, a, x)

# Transformada de Fourier (FFT)
eps = 1e-12  # Pequeno valor para evitar log10(0)
X = np.fft.rfft(x)
freqs_x = np.fft.rfftfreq(len(x), d=1/Fs)
Y = np.fft.rfft(y)
freqs_y = np.fft.rfftfreq(len(y), d=1/Fs)

# Diagnóstico do espectro
print(f"Máximo do espectro de entrada: {np.max(np.abs(X))}")
print(f"Máximo do espectro de saída: {np.max(np.abs(Y))}")

# Gráficos
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(freqs_x, 20 * np.log10(np.abs(X) + eps), label="Entrada")
plt.title("Espectro em frequência do sinal de ENTRADA")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(freqs_y, 20 * np.log10(np.abs(Y) + eps), label="Saída Filtrada", color="orange")
plt.title("Espectro em frequência do sinal de SAÍDA")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
