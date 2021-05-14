import pandas as pd
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
print(data.DESCR)

print('read in dataframe first using the feature data')
df = pd.DataFrame(data.data, columns=data.feature_names)
print(df.head(5))
print('add a target column and fill with target data')
df['target'] = data.target
print(df.head(5))

print('show data type of each column')
print(df.info())
print('show summary stats for each column')
print(df.describe())
print('check target variable properties')
print(df['target'].value_counts())
