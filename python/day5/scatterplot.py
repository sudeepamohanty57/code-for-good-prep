import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("beneficiaries.csv")

plt.scatter(df["age"], df["income"])

plt.title("Age vs Income")
plt.xlabel("Age")
plt.ylabel("Income")
plt.tight_layout()
plt.show()