import pandas as pd

# Load dataset
df = pd.read_excel("data/sample_-_superstore.xls")

# Print first 5 rows
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
# Fill missing values (if any)
df = df.fillna(0)

print("Missing values handled")
print("Before duplicates:", df.duplicated().sum())

df = df.drop_duplicates()

print("After duplicates:", df.duplicated().sum())
print(df.info())
