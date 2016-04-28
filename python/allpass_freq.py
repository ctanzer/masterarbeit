import numpy as np
import matplotlib.pyplot as plt

txtfile = open('./allpass_results.txt', 'w')

f = np.logspace(8, 11, 3000) # frequency range: 100MHz to 100GHz
omega = 2 * np.pi * f

i = 8
for phase_err in [1, .5]:
    R_array = []
    G_array = []
    for R in np.arange(8, 11, .01):
        for G in np.arange(3.3, 4.5, .01):
            RaCa = 1.95e-10
            omega_a = 5.1282e9 # omega_a = 1 / (R_a * C_a)
            omega_b = omega_a * R
            omega_c = omega_b * G
            omega_d = omega_a * G

            delta_phi = -360 / np.pi * (  np.arctan(omega / omega_a) + np.arctan(omega / omega_b)   # Berechnung der Phasenkennlinie fuer 4 Allpaesse
                                        - np.arctan(omega / omega_c) - np.arctan(omega / omega_d) )

            fmin = 900
            while delta_phi[fmin] > (-90 + phase_err) and fmin < 2999: # ermittelt niedrigste Frequenz bei der Phasenkennlinie um weniger als 1° abweicht
                fmin += 1

            fmax = fmin
            while delta_phi[fmax] < (-90 + phase_err) and delta_phi[fmax] > (-90 - phase_err) and fmax < 2999: # hoechste Frequenz mit Abweichung < 1°
                fmax += 1

            if (f[fmax] - f[fmin]) > 5e9:
                txtfile.write("R: {0:2.2f} G: {1:2.2f}".format(R, G))
                txtfile.write("\tf_min: {0:1.5e}\tf_max: {1:1.5e}".format(f[fmin], f[fmax]))
                txtfile.write("\tf_max - f_min: {0:1.5e}\n".format(f[fmax] - f[fmin]))
                R_array.append(R)
                G_array.append(G)

        txtfile.write("---------------------------------------------------------------------------------------------------------\n")
        if R % 1 < .01: # nur um zu sehen wie lange es noch dauert ^^
            print(i)
            i -= 1

    if phase_err == 1:
        plt.plot(R_array, G_array, "bo")
    else:
        plt.plot(R_array, G_array, "go")


txtfile.close()

plt.grid(True)
plt.xlabel("R")
plt.ylabel("G")

plt.show()
