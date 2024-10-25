import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

kody = [
    '1000 0000 0000', '0100 0000 0000', '0010 0000 0000',
    '0001 0000 0000', '0000 1000 0000', '0000 0100 0000',
    '0000 0010 0000', '0000 0001 0000', '0000 0000 1000',
    '0000 0000 0100', '0000 0000 0010', '0000 0000 0001'
]
wartosci_oczekiwane = [8, 4, 2, 1, 0.8, 0.4, 0.2, 0.1, 0.08, 0.04, 0.02, 0.01]
wartosci_zmierzone = [7.964, 3.973, 1.982, 0.994, 0.797, 0.393, 0.193, 0.097, 0.076, 0.038, 0.017, 0.005]

x = np.arange(len(kody))
width = 0.4

plt.figure(figsize=(10, 6))
plt.bar(x - width / 2, wartosci_oczekiwane, width, label='Wartość Oczekiwana [V]', color='blue')
plt.bar(x + width / 2, wartosci_zmierzone, width, label='Wartość Zmierzona [V]', color='orange')

for i, v in enumerate(wartosci_oczekiwane):
    plt.text(x[i] - width / 2, v + 0.02, f"{v:.2f}", ha='center')

for i, v in enumerate(wartosci_zmierzone):
    plt.text(x[i] + width / 2, v + 0.02, f"{v:.2f}", ha='center')

plt.xlabel('Wybrany Kod', fontsize=12)
plt.ylabel('Wartość [V]', fontsize=12)
plt.title('Porównanie Wartości Oczekiwanych i Zmierzonych', fontsize=14)
plt.xticks(x, kody, rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=10)
plt.grid(True)
plt.tight_layout()

tabela1_plot_path = "tabela1a_wykres.png"
plt.savefig(tabela1_plot_path)
plt.clf()

kody_now = [
    '1010 0000 0000', '1001 0000 0000', '0000 1100 0000',
    '0000 1010 0000', '0000 1001 0000', '0000 0000 1000',
    '0000 0000 0100', '0000 1000 0001', '0000 1000 0000',
    '0000 1000 0000'
]
wartosci_oczekiwane_now = [10, 9, 1.2, 1, 0.9, 0.12, 0.1, 0.09, 8.08, 1.08]
wartosci_zmierzone_now = [9.971, 8.983, 1.214, 1.014, 0.917, 0.138, 0.117, 0.105, 8.065, 1.094]

x_now = np.arange(len(kody_now))

plt.figure(figsize=(10, 6))
plt.bar(x_now - width / 2, wartosci_oczekiwane_now, width, label='Wartość Oczekiwana [V]', color='blue')
plt.bar(x_now + width / 2, wartosci_zmierzone_now, width, label='Wartość Zmierzona [V]', color='orange')

for i, v in enumerate(wartosci_oczekiwane):
    plt.text(x[i] - width / 2, v + 0.02, f"{v:.2f}", ha='center')

for i, v in enumerate(wartosci_zmierzone):
    plt.text(x[i] + width / 2, v + 0.02, f"{v:.2f}", ha='center')

plt.xlabel('Wybrany Kod', fontsize=12)
plt.ylabel('Wartość [V]', fontsize=12)
plt.title('Porównanie Wartości Oczekiwanych i Zmierzonych (Nowy Zestaw Danych)', fontsize=14)
plt.xticks(x_now, kody_now, rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=10)
plt.grid(True)
plt.tight_layout()

tabela2_plot_path = "tabela1b_wykres.png"
plt.savefig(tabela2_plot_path)
plt.clf()

napiecia = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
obliczone_wyjsciowe_bin = ['00000000', '00011010', '00110011', '01001101', '01100110', '10000000', '10011010', '10110011', '11001101', '11100110', '11111111']
zmierzone_wyjsciowe_bin = ['00000000', '00001111', '00011111', '00101111', '00110101', '01000010', '01010000', '01011111', '01101111', '01111111', '10000100']

obliczone_wyjsciowe = [int(x, 2) for x in obliczone_wyjsciowe_bin]
zmierzone_wyjsciowe = [int(x, 2) for x in zmierzone_wyjsciowe_bin]

plt.figure(figsize=(10, 6))
plt.plot(napiecia, obliczone_wyjsciowe, label='Wartość Obliczona', marker='o')
plt.plot(napiecia, zmierzone_wyjsciowe, label='Wartość Zmierzona', marker='x')

plt.xlabel('Wartość Napięcia Wejściowego [V]', fontsize=12)
plt.ylabel('Wyjście Cyfrowe (dziesiętnie)', fontsize=12)
plt.title('Porównanie Wyjść Cyfrowych (Obliczonych i Zmierzonych)', fontsize=14)
plt.xticks(napiecia, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=10)
plt.grid(True)
plt.tight_layout()

tabela3_plot_path = "tabela2_wykres.png"
plt.savefig(tabela3_plot_path)

plt.clf()
