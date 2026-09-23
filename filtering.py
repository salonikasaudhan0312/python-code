import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Downloads\archive.zip")
df = df[df["aqi"]>100]
df = df[(df["aqi"]>100) & (df["temperature"]> 30)]
aqi_data = df[(df["aqi"] >100) & (df["temperature"]>30 )] [ ["city", "aqi"]]
print(aqi_data)
print(aqi_data.iloc[0])
print(aqi_data.loc[6])

print(df)