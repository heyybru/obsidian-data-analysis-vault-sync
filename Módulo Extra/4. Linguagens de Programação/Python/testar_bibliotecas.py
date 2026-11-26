import matplotlib
import openpyxl
import pandas as pd
import seaborn

print("pandas     ", pd.__version__)
print("openpyxl   ", openpyxl.__version__)
print("matplotlib ", matplotlib.__version__)
print("seaborn    ", seaborn.__version__)

df = pd.DataFrame({"area": ["RH", "TI"], "headcount": [42, 18]})
df.to_excel("teste.xlsx", index=False)
print(pd.read_excel("teste.xlsx"))
