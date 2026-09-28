import pandas as pd

df = pd.read_csv("students.csv")
print(df)
# print(df.isnull().sum())
# # delete row
# print(df.dropna())

# # delete column
# print(df.dropna(axis=1))

# # fill 0
# print(df.fillna(0))

# # mean
# age_mean = df["age"].mean()
# df["age"] = df["age"].fillna(age_mean)
# print(df)

# # clean data
# cleaned_data = df.copy()
# age_mean = cleaned_data["age"].mean()
# cleaned_data["age"] = cleaned_data["age"].fillna(age_mean)
# print(cleaned_data) 

# # forword fill
# print(df.ffill())

# # backword fill
# print(df.bfill())

# # delete duplicate rows
# print(df.drop_duplicates())

# # data types
# print(df.dtypes)

