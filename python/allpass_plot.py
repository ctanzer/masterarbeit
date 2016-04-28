import numpy as np
import matplotlib.pyplot as plt

f = np.logspace(8, 11, 3000) # frequency range: 100MHz to 100GHz
omega = 2 * np.pi * f

R = 10.75
G = 3.9

omega_a = 5.1282e9 * 1 # omega_a = 1 / (R_a * C_a)
omega_b = omega_a * R
omega_c = omega_b * G
omega_d = omega_a * G

delta_phi = -360 / np.pi * (  np.arctan(omega / omega_a) + np.arctan(omega / omega_b)
                            - np.arctan(omega / omega_c) - np.arctan(omega / omega_d) )

plt.semilogx(f, delta_phi)
plt.grid(True)

plt.show()
