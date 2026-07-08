# cosa rende un fungo velenoso?
#tanto per lavoro

import numpy as np #inutilizzato per ora
import pandas as pd
from sklearn.preprocessing import LabelEncoder

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
#alcune features sono scomparse dovro fare il drop perche hanno un solo valore quinid inutili
#ora fare il label del target? che è class 
#con scikitl
le = LabelEncoder()
df_primo["class"] = le.fit_transform(df_primo["class"])
print(df_primo["class"])
print(le.classes_) #per sapere a cosa corrispondono ora gli 1 e gli 0
