# cosa rende un fungo velenoso?
#tanto per lavoro

import numpy  #inutilizzato per ora
import pandas as pd

# non c'è bisogno di questa riga >>> with open("dataset/mushrooms.csv", "r") as f:
    #file= pd.read_csv(f)
df = pd.read_csv("dataset/mushrooms.csv") #aprire il file csv

df.info()   #info su colonnee righe

print(df.isnull().sum())    #conta i valori mancanti per ogni colonna 