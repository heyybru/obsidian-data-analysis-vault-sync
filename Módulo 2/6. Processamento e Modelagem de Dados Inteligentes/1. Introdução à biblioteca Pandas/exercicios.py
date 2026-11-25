import pandas as pd

print(pd.__version__)
print(pd.__file__)

df = pd.DataFrame({"nome": ["Bruno", "Ana"], "nota": [10, 9]})
df
print(df)
