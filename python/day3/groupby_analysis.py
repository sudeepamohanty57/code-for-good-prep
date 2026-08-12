import pandas as pd

data= {
    "name":["A", "B", "C", "D", "E", "F"],
    "city": ["Bhubaneswar","mumbai","Delhi","mumbai", "Delhi","mumbai"],
    "salary": [30000, 45000, 40000, None, 55000, 45000],
    "department": ["Finance", "Marketing", "Sales", "HR", "Sales", "Finance"]
}

df= pd.DataFrame(data)
print(df.groupby("city")["salary"].mean())

print(df.groupby("city")["salary"].max())

print(df.groupby("city")["name"].count())

result=df.groupby("city")["salary"].mean()

print(result.idxmax())

print(df.groupby("department")["salary"].agg(["sum", "max", "min", "count"]))

print(df.groupby("city", as_index=False)["salary"].mean().sort_values("salary", ascending=False))

