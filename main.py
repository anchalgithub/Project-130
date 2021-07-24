import csv
import pandas as pd

df=pd.read_csv("dwarf_stars.csv")
print("Before cleanup:")
print(df.shape)

del df["Luminosity"]


print("After cleanup:")
print(df.shape)

df.to_csv('main.csv')