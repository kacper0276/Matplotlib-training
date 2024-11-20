import matplotlib.pyplot as plt
import numpy as np

distances = [15, 10, 5, 2]  # w cm
temperatures = [27, 30, 40, 60]  # w °C

distances.append(0)
temperatures.append(132)

plt.figure(figsize=(8, 5))
plt.plot(distances, temperatures, marker='o', label='Temperatura od odległości', color='red')
plt.gca().invert_xaxis()
plt.title('Zależność temperatury od odległości od żarówki')
plt.xlabel('Odległość [cm]')
plt.ylabel('Temperatura [°C]')
plt.grid(True)
plt.legend()
plt.savefig('zad1.png')

masses = [2, 3, 4, 5, 6, 7, 8, 9, 10]  # w kg
resistances = [0.5534 / 1000, 124.81, 51.23, 39.925, 25.56, 22.52, 20.43, 15.69, 14.576]  # w kΩ

plt.figure(figsize=(8, 5))
plt.plot(masses, resistances, marker='o', label='Opór od masy', color='blue')
plt.title('Zależność oporu od masy')
plt.xlabel('Masa [kg]')
plt.ylabel('Opór [kΩ]')
plt.grid(True)
plt.legend()
plt.savefig('zad2.png')