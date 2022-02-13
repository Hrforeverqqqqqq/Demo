import numpy as np


arr=np.array([[1, 2],[3, 4]])
print(arr)

arr1=np.zeros((3,4))
print(arr1)

print(np.ones((2,3)))

print(np.arange(6).reshape(2,3))

print(np.random.rand(2,3))#创建二维随机数组

print(np.random.randint(5, size = (2, 3)))#创建二维随机整数数组

print(np.sum(arr,axis=1))# axis=0 表示对每一列求和

print(np.mean(arr))

print(arr.argsort(axis=0))# 将元素按照行从小到大排序，返回对应位置元素的下标

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
print(np.dot(A,B))

















