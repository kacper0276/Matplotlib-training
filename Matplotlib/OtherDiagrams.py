import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = './osadzeni_w_zakladach_karnych_i_aresztach_sledczych_2.csv'
df = pd.read_csv(file_path, sep=';')

years = df.groupby(["rok", 'rodzaj_osadzenia']).agg({"wartosc": 'sum'}).unstack()

years.columns = years.columns.droplevel(0)

fig, ax1 = plt.subplots(figsize=(10, 10))
years.plot(kind='bar', stacked=False, ax=ax1)

ax1.set_ylabel("Ilość osadzonych")
ax1.set_xlabel("Lata")
ax1.set_xticklabels(years.index, rotation=45)
ax1.legend(title='Rodzaj osadzenia')

for gender in years.columns:
    trend_data = years[gender].dropna()
    z = np.polyfit(trend_data.index, trend_data.values, 1)
    p = np.poly1d(z)
    ax1.plot(trend_data.index, p(trend_data.index), linestyle='--', label=f'Trend - {gender}', linewidth=2)

ax2 = ax1.twiny()
years.plot(kind='line', ax=ax2, linewidth=2)

plt.tight_layout()
plt.savefig("lata_liniowy_i_barh.png")

