import numpy as np

x=np.array([10,12,11,15,100])

print("Mean:", np.mean(x))

print("Median:", np.median(x))

print("Standard deviation:", np.std(x))

q1, q3=np.percentile(x, [25,75])

iqr= q3 - q1

print("Q1:", q1)

print("Q3:", q3)

print("IQR:", iqr)

lower= q1 - 1.5*iqr

upper= q3 + 1.5*iqr

outliers=x[(x<lower) | (x>upper)]

print("Lower bound:", lower)

print("Upper bound:", upper)

print("Outliers:", outliers)
