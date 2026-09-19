import numpy as np
import pandas as pd
np_arr = np.array([[1, 2, 3],[4, 5, 6]])
df = pd.DataFrame(np_arr, columns=["A", "B", "C"])
print(df)
