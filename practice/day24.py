# Day 24: 30 Days of python programming

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

arr = [1, 2, 3, 4, 5]
np_arr = np.array(arr)
print(type(np_arr))
print(np_arr)

np_arr = np.array(arr, float)
print(np_arr)

arr = [0, 1, -1, 0, 0]
np_arr = np.array(arr, bool)
print(np_arr)

arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_arr_2d = np.array(arr_2d)
print(type(np_arr_2d))
print(np_arr_2d)

np_arr = np.array([1, 2, 3, 4, 5])
arr = np_arr.tolist()
print(type(arr))
print(arr)
print(np_arr_2d.tolist())

tup = (1, 2, 3, 4, 5)
np_arr = np.array(tup)
print(type(np_arr))
print(np_arr)

np_arr = np.array([1, 2, 3, 4, 5])
print(np_arr)
print("Shape of np_arr:", np_arr.shape)
print(np_arr_2d)
print("Shape of np_arr_2d:", np_arr_2d.shape)

arr = [-3, -2, -1, 0, 1, 2, 3]
np_int_arr = np.array(arr)
print(np_arr)
print(np_arr.dtype)
np_float_arr = np.array(arr, float)
print(np_float_arr)
print(np_float_arr.dtype)

print("The size of np_arr is", np_arr.size)
print("The size of np_arr_2d is", np_arr_2d.size)

print("Original:", np_arr)
print("Addition:", np_arr + 4)

print("Original:", np_arr)
print("Subtraction:", np_arr - 4)

print("Original:", np_arr)
print("Multiplication:", np_arr * 4)

print("Original:", np_arr)
print("Division:", np_arr / 4)

print("Original:", np_arr)
print("Modulus:", np_arr % 4)

print("Original:", np_arr)
print("Floor division:", np_arr // 4)

print("Original:", np_arr)
print("Exponential:", np_arr ** 4)

print("Whole:", np_arr_2d)
print("First row:", np_arr_2d[0])
print("Second row:", np_arr_2d[1])
print("Third row:", np_arr_2d[2])

print("First column:", np_arr_2d[:, 0])
print("Second column:", np_arr_2d[:, 1])
print("Third column:", np_arr_2d[:, 2])

print("Original:", np_arr_2d)
print("Reversed:", np_arr_2d[::-1, ::-1])

np_zeroes = np.zeros((3, 3))
print(np_zeroes)

np_ones = np.ones((3, 3))
print(np_ones)

print("Original:", np_arr_2d)
print("Reshaped:", np_arr_2d.reshape(1, 9))
print("Flattend:", np_arr_2d.flatten())

print("Addition", np_arr_2d + np_ones)
print("Horizontal append:", np.hstack((np_arr_2d, np_ones)))
print("Vertical append:", np.vstack((np_arr_2d, np_ones)))

rand_float_arr = np.random.random(5)
print(rand_float_arr)

rand_int_arr = np.random.randint(1, 20, 5)
print(rand_int_arr)

norm_arr = np.random.normal(0, 1, 10)
print(norm_arr)

matrix = np.matrix(np.ones((4,4)))
print(matrix)

print(np.arange(0, 11, 2))
print(np.linspace(0, 11, 5))
print(np.linspace(0, 11, 5, False))
print(np.logspace(0, 11, 5))
print(np.logspace(0, 11, 5, False))

print("The size (bytes) of np_arr is", np_arr.itemsize)
print("The size (bytes) of np_arr_2d is", np_arr_2d.itemsize)

norm_arr = np.random.normal(0, 1, 100)
print("Max:", norm_arr.max())
print("Min:", norm_arr.min())
print("Mean:", norm_arr.mean())
print("Variance:", norm_arr.var())
print("Standard deviation:", norm_arr.std())

print("Original:", np_arr_2d)
print("Column with min:", np.amin(np_arr_2d, 0))
print("Column with max:", np.amax(np_arr_2d, 0))
print("Row with min:", np.amin(np_arr_2d, 1))
print("Row with max:", np.amax(np_arr_2d, 1))

print("Tile:", np.tile(np_arr, 2))
print("Repeat:", np.repeat(np_arr, 2))

print(np.random.choice(["a", "e", "i", "o", "u"], 10))

plt.hist(norm_arr)
plt.show()

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("Dot product:", np.dot(x, y))

print("Matrix multiplcation:", np.matmul(np_arr_2d, np_ones))

print("Determinant:", np.linalg.det(np_arr_2d))

temp = np_arr_2d.flatten()
pressure = temp * 3 + 6

plt.plot(temp, pressure)
plt.xlabel("Temperature")
plt.ylabel("Pressure")
plt.title("Temperature vs Pressure")
plt.show()

x = np.random.normal(24, 10, 10000)
ax = sns.displot(x)
ax.set(xlabel = "x", ylabel = "y")
plt.show()