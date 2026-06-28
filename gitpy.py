# cosa rende un fungo velenoso?
#tanto per

import numpy 
import pandas as pd

file = open("dataset/mushrooms.csv", "r") #chissa se funziona 
df = pd.DataFrame(file)

df.info()

df.isnull().sum()