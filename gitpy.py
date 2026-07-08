# cosa rende un fungo velenoso?
#tanto per lavoro

import numpy as np #inutilizzato per ora
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder

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

#proviamo con pandas.. no
df_primo = df.copy()

print(df_primo.nunique()) #per vedere il numero di categorie univoche
#alcune features sono scomparse dovro fare il drop perche hanno un solo valore quinid inutili
#ora fare il label del target? che è class 
#con scikitl
le = LabelEncoder()
df_primo["class"] = le.fit_transform(df_primo["class"]) #èil target
print(df_primo["class"].head(10))
print(le.classes_) #per sapere a cosa corrispondono ora gli 1 e gli 0 (del target)

#droppare features inutili (con 1 solo valore) 
# solo veil-type  
print(df_primo.shape)
df_primo = df_primo.drop("veil-type", axis=1)
print(df_primo.shape)

#ora ohe con pandas (one hot encoding, per ottenere piu colonne con sono 2 valori ciascuno)
df_primo = pd.get_dummies(df_primo)
print(df_primo.shape)
#siamo apassati da 22 a 117 colonne

#da rifare il label encoding per tutte le features
#proviamo questo ordinal encoder
oe = OrdinalEncoder()
df_primo= oe.fit_transform(df_primo)

#df_primo.head()       head() non funziona su numpy array
print(df_primo[:5])
#tanto per vederlo con pandas convertiamolo e poi facciamo head()
jim= pd.DataFrame(df_primo)
print(jim.head())