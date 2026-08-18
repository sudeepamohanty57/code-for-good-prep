import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("beneficiaries.csv")

df["age"].plot(kind="hist", bins=5)

plt.title("Age distribution of beneficiaries")

plt.xlabel("Age")

plt.ylabel("Number of beneficiaries")

plt.tight_layout()

plt.show()
