# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# y =arr.view()
# #arr[0] = 42

# print(arr)
# print(x)
# print(y)
import numpy as np

arr=np.array([3,4,5,67,7,5,6,7])
ar=np.array_split(arr,5)
print(ar)