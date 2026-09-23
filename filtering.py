import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Downloads\archive.zip")
df = df[df["aqi"]>100]
df = df[(df["aqi"]>100) & (df["temperature"]> 30)]
print(df)