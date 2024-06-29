import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

plt.rcParams['font.family'] = 'Times New Roman'

plt.rcParams["figure.figsize"] = (18, 10)


labels = 'Szkoły podstawowe, 6', 'Licea ogólnokształcące, 35', 'Kwalifikacyjne kursy zawodowe, 155'
sizes = [6, 35, 155]
labels = [ '\n'.join(wrap(l, 20)) for l in labels ]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, startangle=140, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%', textprops={'fontsize': 30, 'weight': 'bold'})

plt.title('Osadzeni objęci nauczaniem w szkołach przywieziennych i pozawięziennych')

plt.tight_layout()
plt.savefig("Szkoly.png")