import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i] + 35, y[i], fontweight='bold', fontsize=12, ha = 'center')

plt.rcParams["figure.figsize"] = (12, 10)
fig, ax = plt.subplots()


labels = ['Szkoły podstawowe', 'Szkoły policealne', 'Licea ogólnokształcące', 'Szkoły wyższe', 'Kwalifikacyjne kursy zawodowe', 'Ogółem']
counts = [145, 0, 732, 26, 3743, 4646]
colors = ['tab:blue', 'mediumpurple', 'g', 'lightcoral', 'tab:red', 'orange']

ax.bar(labels, counts, label=labels, color=colors, edgecolor='black')

addlabels(labels,counts)

plt.title('Osadzeni objęci nauczaniem w szkołach przywieziennych i pozawięziennych')
plt.xticks(rotation=45)

ax.legend(title='Rodzaje szkół')

plt.tight_layout()
plt.savefig("Nauczanie.png")