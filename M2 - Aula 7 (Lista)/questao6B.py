import numpy as np
import matplotlib.pyplot as plt

zero = np.roots([1,0.8])
polo = np.roots([1,1,0.41])

plt.figure(figsize=(6, 6))
circulo = plt.Circle((0, 0), 1, color='blue', fill=False, linestyle='--', label='Círculo Unitário')
plt.gca().add_artist(circulo)

plt.scatter(np.real(zero), np.imag(zero), color='green', label='Zeros', s=100)
plt.scatter(np.real(polo), np.imag(polo), color='red', label='Polos', s=100)

plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Polos e Zeros no Plano Complexo z')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
