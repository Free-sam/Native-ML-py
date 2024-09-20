
import pandas as pd

df = pd.read_json('https://www.w3schools.com/python/pandas/data.js')

print(df.to_string())