import pandas as pd

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Check missing values
print(df.isnull().sum())

# Handle missing values

# Age: Fill missing values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Embarked: Fill missing values with mode (most frequent value)
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Cabin: Too many missing values, so drop this column
df.drop("Cabin", axis=1, inplace=True)

# Check if missing values are removed
print("\nMissing values after cleaning:")
print(df.isnull().sum())