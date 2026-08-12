import numpy as np

arr=np.arange(1,21)
print(arr)

print("Shape:", arr.shape)

print("Size:", arr.size)

print("Dimensions:", arr.ndim)

print("Even nums:", arr[arr%2==0])

print("Mean:", np.mean(arr))

print("Median:", np.median(arr))

print("Min value:", np.min(arr))

print("Mean:", np.max(arr))

print("Multiplied by 5:", [5*arr])

print(arr[0])

print(arr[1:5])

print(arr[arr>10])

print(arr *2)

print(arr + 10)

