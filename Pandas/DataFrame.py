import pandas as pd
import numpy as np
info = {
    "Name" : ["Adam", "Eve", "Bob"],
    "Marks" : [78, 99, 85],
    "Grade" : ['B', 'O', 'A']
}

df = pd.DataFrame(info)

print(df)
print(type(df))

print(df.index)        # row labels
print(df.columns)      # column labels

# DataFrom using Numpy array
np_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(np_arr, columns=["Col1", "Col2", "Col3"])
print(df)

# DataFrom using Lists
l = [["Adam", 96], ["Eve", 75], ["Bob", 82], ["Charlie", 92]]
df = pd.DataFrame(l, columns=["Name", "Marks"])
print(df)