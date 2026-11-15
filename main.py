import pandas as pd

df = pd.read_json('./data/posts.json')

df_sample = df.sample(10)

# print(len(df))
# print(df_sample)
print(pd.isna(df))