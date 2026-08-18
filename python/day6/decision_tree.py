import pandas as pd

df=pd.read_csv("beneficiaries.csv")

""" cleaning """

df=df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)

df["age"]=pd.to_numeric(df["age"], errors= "coerce")

df["age"]=df["age"].fillna(df["age"].median())

df["income"]=df["income"].fillna(df["income"].median())

print("\nMissing values after cleaning:")
print(df.isna().sum())

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrices import classification_report

x= df[["age","income"]]
y=df["risk"]

x_train, x_test, y_train, y_test= train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model=DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

model.fit(x_train, y_train)
pred= model.predict(x_test)
print(classification_report(y_test, pred))