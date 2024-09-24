import pandas as pd
df=pd.read_csv('./big-mac-full-index.csv')
# print(df.iloc[2])
print(df)

country_code = 'RUS'

query_text = f"(iso_a3 = '{country_code}')"

# sub_df = df.query(query_text)

print(len(df))
sub_df = df.query(query_text)
print(len(sub_df))
print(sub_df)

print(sub_df.loc[21])
new_query = f"date > '2012-01-01' and date < '2012-12-31'"
new_date_df = df.query(new_query)