import numpy as np
import matplotlib.pyplot as plt
from scipy import signal    

# Definir a frequência de amostragem (exemplo: 8 kHz)
fs = 8000  # Frequência de amostragem em Hz

# Frequências de interesse
frequencies_hz = [100, 1000]  # 100 Hz e 1 kHz

# Converter as frequências para a frequência normalizada (radianos por amostra)
frequencies_normalized = [2 * np.pi * f / fs for f in frequencies_hz]

# Calcular a resposta em frequência nas frequências de interesse
attenuations_db = []
for freq in frequencies_normalized:
    idx = np.argmin(np.abs(w - freq))  # Encontrar o índice mais próximo da frequência desejada
    attenuation_db = 20 * np.log10(abs(h[idx]))
    attenuations_db.append(attenuation_db)

# Exibir os resultados
for f_hz, attenuation_db in zip(frequencies_hz, attenuations_db):
    print(f"Atenuação em {f_hz} Hz: {attenuation_db:.2f} dB")
