import pandas as pd

data={
    "name":["A","B","C","D","E","F"],
    "age": [21, 25, None, 19, 30, 25],
    "city": ["Bhubaneswar","mumbai","Delhi","mumbai", "Delhi","mumbai"],
    "salary": [30000, 45000, 40000, None, 55000, 45000]
}
df=pd.DataFrame(data)

print("First 3:", df.head(3))

print("Shape:", df.shape)

print("Data type:", df.dtypes)

print("Missing values:", df.isna().sum())

df=df.drop_duplicates()

df["age"]=df["age"].fillna(df["age"].median())

df["salary"]=df["salary"].fillna(df["salary"].median())

print(df[df["age"]>=21])

print(df[df["city"]=="Mumbai"])

print(df[(df["city"]=="Mumbai") & (df["salary"]> 40000)])

print(df.sort_values("salary", ascending=False))

print(df["age"])

print(df[["age"]])

print(type(df["age"]))

print(type(df[["age"]]))

print(df[["name", "age"]])
