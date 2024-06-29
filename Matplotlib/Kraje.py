import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i] + 35, y[i], fontweight='bold', fontsize=12, ha = 'center')

plt.rcParams["figure.figsize"] = (12, 10)
fig, ax = plt.subplots()

labels = ['Ukraina', 'Gruzja', 'Białoruś', 'Rosja', 'Mołdawia', 'Rumunia', 'Bułgaria', 'Armenia', 'Niemcy', 'Litwa', 'Słowacja', 'Nigeria', 'Uzbekistan', 'Wietnam', 'Czechy']
counts = [1128, 341, 147, 93, 79, 64, 38, 32, 28, 25, 23, 22, 22, 22, 18]
colors = ['tab:blue', 'indigo', 'g', 'lightcoral', 'tab:red', 'orange', 'tab:grey', 'lavender', 'slateblue', 'plum', 'lightskyblue', 'linen', 'darksalmon', 'tan', 'paleturquoise']

bars = ax.barh(labels, counts, label=labels, edgecolor='black', color=colors)

ax.bar_label(bars)

addlabels(labels,counts)
ax.set_xlabel('Ilość osadonych')
ax.set_ylabel('Narodowość')
plt.title('Obcokrajowi osadzeni')

ax.legend(title='Narodowości')
plt.savefig("narodowosci.png")

