import pandas as pd
df=pd.read_csv('./big-mac-full-index.csv')
df.head()

#index method

# for index in df.index:
#     print(df['date'][index])

#iterrows method

for i, r in df.iterrows():
    print(r['name'],
        r['iso_a3'])
    
#apply method

print(df.apply(lambda row:row['date'], axis = 1))
