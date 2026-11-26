import platform
import sys

import pandas as pd

print("Python:", sys.version.split()[0])
print("Executável:", sys.executable)
print("Sistema:", platform.system())
print("Pandas:", pd.__version__)
