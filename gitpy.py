# cosa rende un fungo velenoso?
#tanto per lavoro

import numpy as np #inutilizzato per ora
import pandas as pd

# non c'è bisogno di questa riga >>> with open("dataset/mushrooms.csv", "r") as f:
    #file= pd.read_csv(f)
df = pd.read_csv("dataset/mushrooms.csv") #aprire il file csv

df.info()   #info su colonnee righe

"""print(df.isnull().sum())    #conta i valori mancanti per ogni colonna (se 0 ovviamente non ne macano quindi il dataset è cmpleto)
print(df.shape)
print(df.isna().sum())
print(df.head())"""
""" fin qua ho solo controllato se il csv è completo
e le info riguardo al cvs, se non fosse stato comppleto qua 
avrei dovuto completarlo in qualche modo e o ripulirlo
"""
# dovro fare label encding mi sa, per trasformare le lettere in 1 e 0 se true o false

#proviamo con pandas
df_primo = df.copy()

print(df_primo.nunique()) #per vedere il numero di categorie univoche
