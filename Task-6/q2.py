from tabnanny import check
import pandas as pd
import numpy as np
missing_values = ["Nan","NA","-","Nil"]
df = pd.read_csv("dataset.csv")

check_null_values = df.isnull().sum()
print("\nMissing values in the given csv file are: ")
print(check_null_values)
print(df[df['BsmtQual'].isnull()])

print("\nMissing values in LotFrontage: \n")
print(df['LotFrontage'].isnull())
print("\nupdated LotFrontage values: \n")
df['LotFrontage'].fillna('empty',inplace = True)
print(df['LotFrontage'])

print("\nMissing values in Alley: \n")
print(df['Alley'].isnull())
print("\nupdated Alley values: \n")
df['Alley'].fillna('empty',inplace = True)
print(df['Alley'])

print("\n")
d = df[df['BsmtQual'].isnull()]
print(d)

print("\nupdated BsmtQual values: \n")
df['BsmtQual'].fillna('empty',inplace = True)
print(df[df['BsmtQual'].isnull()])

print("\n")
d = df[df['BsmtCond'].isnull()]
print(d)

print("\nupdated BsmtCond values: \n")
df['BsmtCond'].fillna('empty',inplace = True)
print(df[df['BsmtCond'].isnull()])

print("\n")
d = df[df['BsmtExposure'].isnull()]
print(d)

print("\nupdated BsmtExposure values: \n")
df['BsmtExposure'].fillna('empty',inplace = True)
print(df[df['BsmtExposure'].isnull()])

print("\n")
d = df[df['BsmtFinType1'].isnull()]
print(d)

print("\nupdated BsmtFinType1 values: \n")
df['BsmtFinType1'].fillna('empty',inplace = True)
print(df[df['BsmtFinType1'].isnull()])

print("\n")
d = df[df['BsmtFinType2'].isnull()]
print(d)

print("\nupdated BsmtFinType2 values: \n")
df['BsmtFinType2'].fillna('empty',inplace = True)
print(df[df['BsmtFinType2'].isnull()])

print("\n\nUpdated final csv file: \n")
print(df.isnull().sum())