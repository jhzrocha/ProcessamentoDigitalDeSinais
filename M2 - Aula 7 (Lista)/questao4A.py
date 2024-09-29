import numpy as np
import matplotlib.pyplot as plt

zero = 1/2
polo = -1/4

plt.figure(figsize=(6, 6))
circle = plt.Circle((0, 0), 1, color='blue', fill=False, linestyle='--', label='Círculo Unitário')
plt.gca().add_artist(circle)

plt.scatter(np.real(zero), np.imag(zero), color='green', label='Zero', s=100)

plt.scatter(np.real(polo), np.imag(polo), color='red', label='Polo', s=100)

plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Polos e Zeros no Plano Complexo z')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
