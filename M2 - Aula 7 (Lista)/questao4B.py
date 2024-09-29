import numpy as np
import matplotlib.pyplot as plt

zero = 0

polo1 = 0.305
polo2 = 1.6385

plt.figure(figsize=(6, 6))
circle = plt.Circle((0, 0), 1, color='blue', fill=False, linestyle='--', label='Círculo Unitário')
plt.gca().add_artist(circle)

plt.scatter(np.real(zero), np.imag(zero), color='green', label='Zero', s=100)

plt.scatter(np.real(polo1), np.imag(polo1), color='red', label='Polo1', s=100)
plt.scatter(np.real(polo2), np.imag(polo2), color='red', label='Polo1', s=100)

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
