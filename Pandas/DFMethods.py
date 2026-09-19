import numpy as np
import pandas as pd
data_list = {
    "Name" : ['John', 'Anna', 'Peter', 'Linda'],
    "Age" : [28, 40, 29, 42],
    "City" : ['New york', 'Paris', 'Bareli', 'Londan'],
    "Salary" : [6500, 3400, 62000, 85000]
}
df2 = pd.DataFrame(data_list)
# print(df2.head(2))
# print(df2.tail(2))
# print(df2.sample())
# print(df2.info())
# print(df2.shape)
# print(df2.describe())
# print(df2.columns)
print(df2.nunique())


