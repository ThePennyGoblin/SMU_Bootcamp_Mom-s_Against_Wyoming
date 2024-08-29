import pandas as pd

csv = pd.read_csv("Batting.csv")

df = pd.DataFrame(csv)


# print(df.dtypes)
print(df.columns)
print(df["playerId","Season"].value_counts())
print(df["Name"].value_counts())
