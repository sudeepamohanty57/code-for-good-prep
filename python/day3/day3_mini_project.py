import pandas as pd

df=pd.read_csv("beneficiaries.csv")

print("The first 5 rows: ")
print(df.head(5))

print("shape:", df.shape)

print("Column names:")
print(df.columns)

print("Information:")
print(df.info())

print("\nMissing values:")
print(df.isna().sum())

print("Duplicate rows:")
print(df.duplicated().sum())

""" cleaning """

df=df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)

df["age"]=pd.to_numeric(df["age"], errors= "coerce")

df["age"]=df["age"].fillna(df["age"].median())

df["income"]=df["income"].fillna(df["income"].median())

print("\nMissing values after cleaning:")
print(df.isna().sum())

""" Filter beneficiaries """

adults=df[df["age"]>18]

print("\nAdult beneficiaries:")
print(adults)

print("\nNumber of adults:", len(adults))

# 13. Number of beneficiaries by city
city_count = (
    df.groupby("city")
      .size()
      .sort_values(ascending=False)
)

print("\nBeneficiaries by city:")
print(city_count)

# 14. Average income by city
average_income = df.groupby("city")["income"].mean().sort_values(ascending=False)

print("\nAverage income by city:")
print(average_income)

print("\nCity with highest average income:")
print(average_income.idxmax())

service_count = (
    df.groupby("service")
    .size()
    .sort_values(ascending=False)
)

print("\nBeneficiaries by service:")
print(service_count)

service_income= (
    df.groupby("service")["income"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage income by service:")
print(service_income)

""" Filter a specific group """

low_income_adults=df[
    (df["age"]>=18) &
    (df["income"]< 30000)
]

print("\nAdults with income below 30000:")
print(low_income_adults)

""" Sort the beneficiaries """

highest_income= df.sort_values(
    "income",
    ascending = False
)
print("\nBeneficiaries sorted by income:")
print(highest_income)

# Generate useful insights

most_common_city = df["city"].value_counts().idxmax()
highest_income_city = df.groupby("city")["income"].mean().idxmax()
most_common_service = df["service"].value_counts().idxmax()

print("\n========== KEY INSIGHTS ==========")

print("1. Most beneficiaries are from:", most_common_city)

print("2. City with highest average income:",
      highest_income_city)

print("3. Most common service received:",
      most_common_service)