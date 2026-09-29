import pandas as pd
import matplotlib as plt

filepath = "./BIOL 363 Mussel MR Lab 09262026 Class data.xlsx"

df = pd.read_excel(filepath, header=[0,1], skiprows=3)
# print(df.columns)

# ======================
# Outliers



# ======================
# Figure