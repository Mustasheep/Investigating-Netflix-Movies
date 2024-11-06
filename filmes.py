import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importando o CSV da Netflix como um DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
print(netflix_df.head())
print(netflix_df.info())
print(netflix_df.shape())
print(netflix_df.describe())

# Filtrando as colunas que serão úteis no projeto
filmes_filtrados = netflix_df[["title", "release_year", "duration", "genre"]]

# Modelando dados e preparando para análise
filmes_1990 = filmes_filtrados[np.logical_and(filmes_filtrados["release_year"] >= 1990,filmes_filtrados["release_year"] <= 1999)].sort_values(by='release_year')
print(filmes_1990.to_string(index=False))

# Calculando a mediana da duração dos filmes
median = int(np.median(filmes_1990["duration"]))

# Representação gráfica
plt.hist(filmes_1990['duration'], bins=10, color='#009944')
plt.axvline(median, color='blue', linestyle='dashed', linewidth=2)
plt.xlabel('Tempo em minutos')
plt.ylabel('Filmes')
plt.title('Duração de filmes da década de 90')
plt.show()
print(f"\nA duração mais frequente dos filmes na década de 90 é de {median} minutos.")

# Filmes de ação considerados curtos
movie_count = []

for index, row in filmes_1990.iterrows():
    if row['duration'] < 90 and row['genre'] == 'Children':
        movie_count.append(row['title'])
    short_movie_count = len(movie_count)

print("Os filmes infantis considerados curtos são:\n")
for i, filme in enumerate(movie_count, start=1):
    print(f"{i}. {filme}")
