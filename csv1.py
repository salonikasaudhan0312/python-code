# AQI data set
import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Downloads\archive.zip")
# columns
# print(df["city"])
# print(df[["city", "aqi"]])

# row
# print(df.loc[2])     
# print(df.loc[0:2])
# print(df.iloc[0:2])

# cells - row, columns
print(df.loc[0:2, ["city","aqi"]])
