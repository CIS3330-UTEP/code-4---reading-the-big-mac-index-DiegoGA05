### Queries
import pandas as pd

filename = './big-mac-full-index.csv'
df = pd.read_csv(filename)

# print(df['dollar_price'])

query = f"(iso_a3 == 'MEX')"
mxn_df = df.query(query)

### Various print queries

# print(mxn_df['dollar_price'].min())
# print(mxn_df['dollar_price'].max())
# print(round(mxn_df['dollar_price'].mean(),2))
# print(mxn_df)
# print(mxn_df.median())
# print(type(mxn_df['dollar_price'].mean(),2))

### Row Queries

query = f"(iso_a3 == 'JPN')"
jpn_df = df.query(query)
min_idx = jpn_df['dollar_price'].idxmin()
# # min_idx = jpn_df['dollar_price'].idxmax()

print(min_idx)
print(jpn_df.loc[min_idx])
# print(jpn_df.loc[min_idx]['dollar_price'])
