import matplotlib.pyplot as plt
import numpy as np

# Créez des données pour la moitié de la sinusoïde
x = np.linspace(0, 2 * np.pi, 1000)  # Valeurs de x de 0 à 2*pi
y = np.sin(x[:len(x)//2])  # Moitié de sinusoïde (0 à pi)

# Trouvez l'amplitude maximale de la sinusoïde
amplitude_max = np.max(y)
x_amplitude_max = x[np.argmax(y)]

# Créez le graphe
plt.figure(figsize=(8, 4))

# Tracez la moitié de la sinusoïde
plt.plot(x[:len(x)//2], y, label='Moitié de Sinusoïde')

# Tracez des traits non continus pour couper l'axe x et y au point d'amplitude maximale
plt.plot([x_amplitude_max, x_amplitude_max], [0, amplitude_max], 'r--')
plt.plot([0, x_amplitude_max], [amplitude_max, amplitude_max], 'r--')

# Ajoutez une flèche indiquant la direction de la vitesse de l'onde
plt.annotate('Vitesse', xy=(x_amplitude_max, amplitude_max), xytext=(x_amplitude_max + 1, amplitude_max),
             arrowprops=dict(arrowstyle='->'), fontsize=12)

# Masquez les graduations des axes
plt.xticks([])
plt.yticks([])

# Affichez le graphe
plt.show()

plt.savefig("graphe_1.pdf")