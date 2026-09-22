import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titanic Data Analysis Project
# Place train.csv (or titanic.csv) in this folder before running.

FILE = "titanic.csv"
df = pd.read_csv(FILE)

print("Dataset loaded successfully!")
print(df.head())
print("\nShape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

# Basic cleaning for analysis
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

print("\nOverall survival rate:")
print(df["Survived"].mean() * 100)

print("\nSurvival rate by sex:")
print(df.groupby("Sex")["Survived"].mean().mul(100).round(2))

print("\nSurvival rate by passenger class:")
print(df.groupby("Pclass")["Survived"].mean().mul(100).round(2))

print("\nSurvival rate by embarkation port:")
print(df.groupby("Embarked")["Survived"].mean().mul(100).round(2))

# 1. Survival count
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Survived")
plt.title("Titanic Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Passengers")
plt.tight_layout()
plt.savefig("images/survival_count_from_csv.png", dpi=180)
plt.show()

# 2. Survival by sex
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x="Sex", y="Survived")
plt.title("Survival Rate by Sex")
plt.ylabel("Survival Rate")
plt.tight_layout()
plt.savefig("images/survival_by_sex_from_csv.png", dpi=180)
plt.show()

# 3. Survival by class
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x="Pclass", y="Survived")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.tight_layout()
plt.savefig("images/survival_by_class_from_csv.png", dpi=180)
plt.show()

# 4. Age distribution
plt.figure(figsize=(9, 6))
sns.histplot(data=df, x="Age", bins=30, kde=True)
plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("images/age_distribution_from_csv.png", dpi=180)
plt.show()

# 5. Fare vs survival
plt.figure(figsize=(9, 6))
sns.boxplot(data=df, x="Survived", y="Fare")
plt.title("Fare Distribution by Survival")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Fare")
plt.tight_layout()
plt.savefig("images/fare_vs_survival_from_csv.png", dpi=180)
plt.show()

print("\nAnalysis completed successfully!")
