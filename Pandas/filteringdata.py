import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Downloads\archive.zip")
# Filtering Data
print(df[df["aqi"] > 100])
print(df[df["aqi"] > 100][["city", "aqi"]])

print(df[(df["aqi"] > 100) & (df["timestamp"] == "2025-11-04 18:25:17.554219")])
aqi_data = df[(df["aqi"] > 100) & (df["timestamp"] == "2025-11-04 18:25:17.554219")][["city", "aqi"]]

# Difference in loc & iloc - both give same value
print(aqi_data.loc[360]) 
print(aqi_data.iloc[1])

# Query - returns a copy, not a view
print(df.query("aqi > 100 & timestamp == '2025-11-04 18:25:17.554219'"))

my_country = "IN"
print(df.query("country == @my_country"))

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["date"] = df["timestamp"].dt.date
selected_date = pd.to_datetime("2025-11-04").date()

print(df.query("country == @my_country & date == @selected_date & aqi > 100"))

# Use .copy() to avoid confusion
countries = df[["country", "aqi"]].copy()
countries.loc[0:4, "country"] = "India"

print(countries)