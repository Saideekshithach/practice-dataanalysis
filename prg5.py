import pandas as pd
s=pd.Series([10,20,30,40])
print(s)
data={'Name':['Alice','Bob','charlie'],
      'Age':[25,45,23],
      'city':['Newyork','London','Paris']}
df=pd.DataFrame(data)
print(df)
c=df.to_csv('data.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.describe())
print(df.columns)
print(df['Age'])
print(df[['Name','city']])
print(df[df['Age']>28])
print(df.iloc[1])
print(df.loc[1])
df['Age']+=1
print(df['Age'])
df['Country']='USA'
print(df)

df.rename(columns={'Age':'years'},inplace=True)
print(df)
df.drop('city',axis=1)
print(df)



