import pandas as pd

df  = pd.read_json('user_info.json')

print(df.columns.tolist())