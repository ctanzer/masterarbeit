import numpy as np
import matplotlib.pyplot as plt

txtfile = open('./allpass_results.txt', 'w')

f = np.logspace(8, 11, 3000) # frequency range: 100MHz to 100GHz
omega = 2 * np.pi * f

for R in np.arange(7, 12, .05):
    for G in np.arange(3, 5, .05):
        RaCa = 1.95e-10
        omega_a = 5.1282e9 # omega_a = 1 / (R_a * C_a)
        omega_b = omega_a * R
        omega_c = omega_b * G
        omega_d = omega_a * G

        delta_phi = -360 / np.pi * (  np.arctan(omega / omega_a) + np.arctan(omega / omega_b)   # Berechnung der Phasenkennlinie fuer 4 Allpaesse
                                    - np.arctan(omega / omega_c) - np.arctan(omega / omega_d) )

        fmin = 0
        while delta_phi[fmin] > -89 and fmin < 2999: # ermittelt niedrigste Frequenz bei der Phasenkennlinie um weniger als 1° abweicht
            fmin += 1

        fmax = fmin
        while delta_phi[fmax] < -89 and delta_phi[fmax] > -91 and fmax < 2999: # hoechste Frequenz mit Abweichung < 1°
            fmax += 1

        if (f[fmax] - f[fmin]) > 6e9:
            txtfile.write("R: {0:2.2f} G: {1:2.2f}".format(R, G))
            txtfile.write("\tf_min: {0:1.5e}\tf_max: {1:1.5e}".format(f[fmin], f[fmax]))
            txtfile.write("\tf_max - f_min: {0:1.5e}\n".format(f[fmax] - f[fmin]))

    print(R) # nur um zu sehen wie lange es noch dauert ^^
    
txtfile.close()
