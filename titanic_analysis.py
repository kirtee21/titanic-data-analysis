import pandas as pd

# Load Dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Data Cleaning
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df.drop("Cabin", axis=1, inplace=True)

# 1. Who survived more: males or females?

print("Who survived more: males or females?")

survived_gender = df[df["Survived"] == 1]["Sex"].value_counts()

print(survived_gender)


# 2. Did passenger class affect survival chances?

print("\nDid passenger class affect survival chances?")

survival_by_class = df.groupby("Pclass")["Survived"].mean() * 100

print(survival_by_class)


# 3. What was the survival rate by age group?

print("\nWhat was the survival rate by age group?")

# Create age groups
df["Age Group"] = pd.cut(
    df["Age"],
    bins=[0, 12, 18, 35, 60, 100],
    labels=["Child", "Teen", "Adult", "Middle Age", "Senior"]
)

survival_by_age = df.groupby("Age Group")["Survived"].mean() * 100

print(survival_by_age)