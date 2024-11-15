import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import kaiser, freqz, lfilter

# Parâmetros do filtro
fs = 16000           # Frequência de amostragem do áudio em Hz
fc = 150             # Frequência de corte do filtro em Hz
N = 101              # Ordem do filtro (número de coeficientes)
attenuation = 60     # Atenuação mínima desejada na faixa de rejeição em dB

# Caminhos dos arquivos
input_path = 'M2 - Prova 2/Questão 3/Anexo_42011658.pcm'  # Arquivo de entrada
output_path = 'M2 - Prova 2/Questão 3/Sai_Q3_voz_ruido.pcm'  # Arquivo de saída

# Frequência de corte normalizada
fc_normalized = fc / (fs / 2)

# Geração do filtro passa-alta usando a função sinc e janela Kaiser
n = np.arange(N) - (N - 1) / 2
h_lowpass = np.sinc(2 * fc_normalized * n)
h_highpass = -h_lowpass
h_highpass[int((N - 1) / 2)] += 1

# Aplicar a janela Kaiser
beta = 5.65326  # Beta para Kaiser, ajustado para -60 dB
window = kaiser(N, beta)
h_highpass_windowed = h_highpass * window

# Carregar o áudio do arquivo .pcm
with open(input_path, 'rb') as f:
    audio_data = np.frombuffer(f.read(), dtype=np.int16)

# Aplicar o filtro ao áudio
filtered_audio = lfilter(h_highpass_windowed, 1, audio_data)

# Converter o áudio filtrado de volta para int16 para salvar
filtered_audio_int16 = np.int16(filtered_audio)

# Salvar o áudio filtrado em um novo arquivo .pcm
with open(output_path, 'wb') as f:
    f.write(filtered_audio_int16.tobytes())

# Plotar os sinais de entrada e saída
t = np.arange(len(audio_data)) / fs
plt.figure(figsize=(12, 6))

# Sinal de entrada
plt.subplot(2, 1, 1)
plt.plot(t, audio_data, label='Sinal de Entrada')
plt.title('Sinal de Entrada')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.legend()

# Sinal filtrado
plt.subplot(2, 1, 2)
plt.plot(t, filtered_audio, label='Sinal Filtrado (Passa-Alta)', color='orange')
plt.title('Sinal Filtrado')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()

# Carregar o áudio do arquivo .pcm
with open(input_path, 'rb') as f:
    audio_data = np.frombuffer(f.read(), dtype=np.int16)

# Número de amostras
n = len(audio_data)

# Calcular a FFT
audio_fft = np.fft.fft(audio_data)
audio_fft = np.abs(audio_fft)  # Pegamos apenas a magnitude

# Gerar o eixo de frequências
freqs = np.fft.fftfreq(n, d=1/fs)

# Plotar apenas a metade positiva da FFT (pois é simétrica)
plt.figure(figsize=(12, 6))
plt.plot(freqs[:n // 2], audio_fft[:n // 2])  # Apenas frequências positivas
plt.title('Representação em Frequência do Áudio')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.show()
