import pandas as pd

data={
    "name":["A","B","C","D","E","F"],
    "age": [21, 25, None, 19, 30, 25],
    "city": ["Bhubaneswar","mumbai","Delhi","mumbai", "Delhi","mumbai"],
    "salary": [30000, 45000, 40000, None, 55000, 45000]
}
df=pd.DataFrame(data)

print("Missing values:", df.isna().sum())

print("Duplicates:", df.duplicated().sum())

df=df.drop_duplicates()

""" Numeric conversion """

df["age"]= df["age"].astype(str)

df["age"]= pd.to_numeric(df["age"], errors = "coerce")

""" String cleaning """

df["city"]= df["city"].str.strip()

df["city"]= df["city"].str.title()

""" Date conversion """

df["date"]= df["date"].todatetime(df["date"], errors= "coerce")

