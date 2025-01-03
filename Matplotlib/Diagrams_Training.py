import matplotlib.pyplot as plt
import seaborn as sns

# Dane do wykresów
proby_samobojcze_2023 = {"7–12 lat": 78, "13–18 lat": 1916}
samobojstwa_2023 = {"7–12 lat": 7, "13–18 lat": 138}

dynamika_proby = {"2021": 1496, "2022": 1937, "2023": 1994}
dynamika_samobojstwa = {"2021": 124, "2022": 156, "2023": 145}

czynniki_internet = {
    "Ekspozycja na treści samobójcze": 50,
    "Wpływ algorytmów": 30,
    "Pakty samobójcze": 10,
    "Podżeganie do samobójstw": 20,
    "Romantyzacja śmierci": 40,
}

# Wykres 1: Liczba prób samobójczych w podziale na grupy wiekowe (2023)
plt.figure(figsize=(8, 5))
sns.barplot(x=list(proby_samobojcze_2023.keys()), y=list(proby_samobojcze_2023.values()), palette="Blues")
plt.title("Liczba prób samobójczych w podziale na grupy wiekowe (2023)")
plt.ylabel("Liczba prób")
plt.xlabel("Grupy wiekowe")
plt.show()

# Wykres 2: Liczba samobójstw w podziale na grupy wiekowe (2023)
plt.figure(figsize=(8, 5))
sns.barplot(x=list(samobojstwa_2023.keys()), y=list(samobojstwa_2023.values()), palette="Reds")
plt.title("Liczba samobójstw w podziale na grupy wiekowe (2023)")
plt.ylabel("Liczba samobójstw")
plt.xlabel("Grupy wiekowe")
plt.show()

# Wykres 3: Dynamika liczby prób samobójczych w latach 2021–2023
plt.figure(figsize=(8, 5))
sns.lineplot(x=list(dynamika_proby.keys()), y=list(dynamika_proby.values()), marker="o", label="Próby samobójcze")
plt.title("Dynamika liczby prób samobójczych w latach 2021–2023")
plt.ylabel("Liczba prób")
plt.xlabel("Rok")
plt.legend()
plt.show()

# Wykres 4: Dynamika liczby samobójstw w latach 2021–2023
plt.figure(figsize=(8, 5))
sns.lineplot(x=list(dynamika_samobojstwa.keys()), y=list(dynamika_samobojstwa.values()), marker="o", color="red", label="Samobójstwa")
plt.title("Dynamika liczby samobójstw w latach 2021–2023")
plt.ylabel("Liczba samobójstw")
plt.xlabel("Rok")
plt.legend()
plt.show()

# Wykres 5: Wpływ czynników związanych z internetem na zachowania samobójcze
plt.figure(figsize=(10, 6))
sns.barplot(x=list(czynniki_internet.keys()), y=list(czynniki_internet.values()), palette="Purples")
plt.title("Wpływ czynników związanych z internetem na zachowania samobójcze")
plt.ylabel("Intensywność wpływu")
plt.xlabel("Czynniki")
plt.xticks(rotation=45)
plt.show()