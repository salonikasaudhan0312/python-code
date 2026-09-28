# AQI data set
import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Downloads\archive.zip")
print(df["country"])
print(df[["city", "aqi"]])

# Select rows (by label)
print(df.loc[0])             # 1st row (by label)
print(df.loc[0:3])           # row0 to row3 - both inclusive in loc

# Select rows (by index)
print(df.iloc[0])            # 1st row 
print(df.iloc[4:7])          # 1st row 

# Select rows & columns
print(df.loc[0, "country"])  # 0th row & specific column
print(df.iloc[0, 2])         # 1th row & 3rd column (by position)

print(df.iloc[0, 1:5])
print(df.loc[0, ["country", "aqi"]])

print(df.loc[0:5, ["country", "city", "latitude"]])   # end is inclusive
print(df.iloc[0:5, 1:3])                              # end is exclusive 

# Select single scalar value
print(df.at[0, "city"])
print(df.iat[0, 2])