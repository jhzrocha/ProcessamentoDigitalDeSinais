import numpy as np
from scipy.signal import iirnotch, filtfilt
import matplotlib.pyplot as plt

# Parâmetros do filtro rejeita-faixa
f0 = 800  # Frequência central a ser rejeitada (exemplo: 60 Hz para ruído de linha)
Q = 30   # Fator de qualidade (ajuste conforme necessário)
fs = 16000  # Frequência de amostragem do áudio em Hz (ajuste conforme necessário)

# Caminhos dos arquivos .pcm
input_path = 'M2 - Prova 2/Questão 2/Anexo_42011635.pcm'
output_path = 'M2 - Prova 2/Questão 2/filtered_audio.pcm'


import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
fs = 16000  # Frequência de amostragem do áudio em Hz (ajuste conforme necessário)

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

# Projeto do filtro rejeita-faixa
b, a = iirnotch(f0, Q, fs)

# Carregar o áudio do arquivo .pcm
with open(input_path, 'rb') as f:
    # Lê o arquivo como uma sequência de inteiros de 16 bits
    audio_data = np.frombuffer(f.read(), dtype=np.int16)

# Aplicar o filtro ao áudio
filtered_audio = filtfilt(b, a, audio_data)

# Converter o áudio filtrado de volta para int16 para salvar
filtered_audio = np.int16(filtered_audio)

# Salvar o áudio filtrado em um novo arquivo .pcm
with open(output_path, 'wb') as f:
    f.write(filtered_audio.tobytes())

# Visualizar o áudio original e filtrado
t = np.arange(len(audio_data)) / fs
plt.figure(figsize=(12, 6))

# Sinal original
plt.subplot(2, 1, 1)
plt.plot(t, audio_data, label='Original')
plt.title('Áudio Original')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.legend()

# Sinal filtrado
plt.subplot(2, 1, 2)
plt.plot(t, filtered_audio, label='Filtrado', color='orange')
plt.title('Áudio Filtrado')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
