import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("beneficiaries.csv")

summary= df.groupby("city")["beneficiary_id"].count()

summary.sort_values(ascending=False,).plot(kind="bar")

plt.title("Beneficiaries by city")

plt.xlabel("city")

plt.ylabel("Number of beneficiaries")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
