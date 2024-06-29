import textwrap
import shutil
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'

df = pd.read_excel('./Badania.xlsx', sheet_name='Worksheet')

categorical_columns = df.select_dtypes(include=['object']).columns

threshold = 7

fig, axes = plt.subplots(len(categorical_columns), 1, figsize=(20, 8 * len(categorical_columns)))

terminal_width = shutil.get_terminal_size().columns

for i, column in enumerate(categorical_columns):
    ax = axes[i]

    split_series = df[column].dropna().str.split(';').explode()

    counts = split_series.value_counts()

    if len(counts) <= threshold:
        labels = [f'{category}\n{count} ({count / counts.sum() * 100:.1f}%)' for category, count in
                  zip(counts.index, counts)]
        ax.pie(counts, labels=labels, startangle=140, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')
        ax.set_title('\n'.join(textwrap.wrap(f'{column}', width=terminal_width)), fontsize=14, fontweight='bold')
    else:
        wrapped_labels = [textwrap.fill(label, width=30) for label in counts.index]

        ax.barh(wrapped_labels, counts, color='skyblue')
        for j, (count, label) in enumerate(zip(counts, counts.index)):
            ax.text(count, j, f' {count} ({count / counts.sum() * 100:.1f}%)', va='center', fontsize=10)
        ax.set_title('\n'.join(textwrap.wrap(f'{column}', width=terminal_width)), fontsize=14, fontweight='bold')
        ax.margins(y=0.1)
        ax.tick_params(axis='y', labelsize=9)

plt.tight_layout()

plt.savefig("nazwa.png")