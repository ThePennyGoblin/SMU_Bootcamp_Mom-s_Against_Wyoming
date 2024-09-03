import pandas as pd
# pd.set_option("display.max_columns", None, "display.max_rows", None)
csv1 = pd.read_csv("data/Batting.csv")
csv2 = pd.read_csv("data/Pitching.csv")

df = pd.DataFrame(csv2)
year = 2023
df = df[df["Season"] == year]
print(df)
df.to_csv(f"pitching{year}.csv")




