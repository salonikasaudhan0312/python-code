import pandas as pd
import numpy as np
df = pd.read_json(r"C:\Users\HP\OneDrive\Desktop\python\Pandas\airports.json")
f = pd.DataFrame(df)
print(f)