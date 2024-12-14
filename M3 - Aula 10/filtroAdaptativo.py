import numpy as np
import matplotlib.pyplot as plt

w = [0,0,0,0]
read_path = 'Prova 1/Anexo_41743449.pcm'


with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    # w = data_i

    convDegrauUnitarioEVetor = np.convolve(w, data_i)
    d = np.sum(w*data_i)
    tama = len(degrauUnitario) + len(vetor) - 1
    tamb = len(impulsoUnitário) + len(vetor) - 1
    n1 = np.arange(0, tama)
    n2 = np.arange(0, tamb)

