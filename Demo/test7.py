
# array = [1,2,3,4,5,6]

# 二分查找
def binary_search(item,arr):
    sta=0
    end=len(arr)-1
    while sta<=end:
        mid=(sta+end)//2
        if item==arr[mid]:
            return True
        elif item<arr[mid]:
            end=mid-1
        else:
            sta=mid+1
# print(binary_search(2,array))

# 插入排序
# 简单来说，先定义一个有序队列，
# 然后把无序队列中的第一个元素放到有序队列的合适位置，
# 重复操作，直至形成一个完整的有序队列
def insert_sort(alist):
    n = len(alist)
    for j in range(0, n):
        for i in range(j, 0, -1):#从列表下标为j的元素开始往后取
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            else:
                break
    return alist

#
# if __name__ == '__main__':
#     alist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#     insert_sort(alist)
#     print("排序后：", alist)

#选择排序
# 它的工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，
# 存放在序列的起始位置
def SelectSort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]
    return arr

# print(SelectSort([11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22]))





#  斐波那契数列
def fbnq(n):
    if n<2:
        return n
    return fbnq(n-1)+fbnq(n-2)

def fbnq1(n):
    fib_n=0
    fib_one=1
    fib_two=0
    res=[0,1]
    if n<2:
        return res[n]
    for i in range(2,n+1):
        fib_n=fib_one+fib_two
        fib_two=fib_one
        fib_one=fib_n
    return fib_n


def find_dup(arr):
    not_dup =set()
    dup=set()
    for x in arr:
        if x not in not_dup:
            not_dup.add(x)
        else:
            dup.add(x)
    return dup

# isdigit()方法检测字符串是否只由数字组成。
# a = ['a', 1, 2, 'b']
# for x in a:
#     if str(x).isdigit():
#         print(x)


# 冒泡排序

def bubble_sort(arr):
    n = len(arr)
    if len(arr) < 2:
        return arr
    for i in range(n - 1):
        count = 0
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
        if count == 0:
            return arr
    return arr
# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-1):
#             if arr[i]<arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#     return arr
# arr1 = [2, 1, 5, 3, 6]
# print(bubble_sort(arr1))

# 快排
# 快速排序使用分治的思想，通过一趟排序将待排序列分割成两部分，
# 其中一部分记录的关键字均比另一部分记录的关键字小。
# 之后分别对这两部分记录继续进行排序，以达到整个序列有序的目的。
def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        prv=arr[0]
        less=[i for i in arr[1:] if i<=prv]#列表生成式
        more=[i for i in arr[1:] if i>prv]
    return quick_sort(less)+[prv]+quick_sort(more)


array = [2, 1, 6, 3, 4, 5]
# print(quick_sort(array))

# li1=[]
# for i in range(1,11):
#     li1.append(i*i)
# print(li1)
# li2=[j*j for j in range(1,11)]
# print(li2)

# 拓扑排序

import pdb
def toposort(G):
    cnt=dict((u,0) for u in G.keys())
    pdb.set_trace()#设置追踪断点
    for u in G:
        for v in G[u]:
            cnt[v]+=1
    Q=[u for u in cnt.keys() if cnt[u]==0]
    seq=[]
    while Q:
        s=Q.pop()
        seq.append(s)
        for u in G[s]:
            cnt[u] -=1
            if cnt[u]==0:
                Q.append(u)
    return seq

G = {
    'a': {'b', 'f'},
    'b': {'c', 'd', 'f'},
    'c': {'d'},
    'd': {'e', 'f'},
    'e': {'f'},
    'f': {}
}

# res = toposort(G)
# print(res)

# def binary_plus(a, b):
#     a, b = int('0b' + a, 2), int('0b'+b, 2)
#     return bin(a + b)[2:]
#
#
# if __name__ == '__main__':
#     a = '11'
#     b = '1'
#     print(binary_plus(a, b))


def some_sort(arr):
    lef=[]
    rig=[]
    for i in arr:
        if i=='+':
            lef.append(i)
        else:
            rig.append(i)
    lef.extend(rig)
    print(lef.extend(rig))
    return lef

# print(some_sort(['+','-','+']))



class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

#链表逆转
def reverse_node(head):
    p=head
    q=head.next
    head.next=None
    while q:
        r=q.next
        q.next=p
        p=q
        q=r
    head=p
    return head

# if __name__ == '__main__':
#     l1 = ListNode(3)
#     l1.next = ListNode(2)
#     l1.next.next = ListNode(1)
#
#     l = reverse_node(l1)
#     print(l.val, l.next.val, l.next.next.val)





# a=[1,2,3]
# b=[1,2,4]
# print(id(a[1])==id(b[1]))
# print(id(a[1]))

# def w1():
#     print('正在装饰')
#     def inner():
#         print('正在验证权限')
#     return inner()
# w1()


# print([i for i in range(3)])
# print((i for i in range(3)))
#
# tup = (1,2,[3,4])
# tup[2].extend([5,6])
# print(tup)
#
# a1=[1,2,3,4]
# a1.extend([1,2])
# print(a1)

# lis=[1,2,3,4,5,6]
#
# print(lis[-1:1:-1])
# print(lis[:-1])
# print(lis[5:1:-1])
# print(lis[5:2:-1])#取不到终止索引值，列表切片起止索引，终止索引，步长(-1为反向获取)


# def bar(multiple):
#     def foo(n):
#         return multiple ** n
#     return foo
#
#
# print(bar(2)(3))


# tmp = dict.fromkeys(['a', 'b'], 4)#fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值
# print(tmp)

# print({x:x*x for x in range(6)})

# print([x for x in range(101) if x%2==0])

import pandas as pd
import numpy as np
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# df =pd.DataFrame(data,index=labels)
#
# print(df)

s_1 = pd.Series(data['animal'])
s_2 = pd.Series(data['age'])
s_3 = pd.Series(data['visits'])
s_4 = pd.Series(data['priority'])
pd_2 = pd.DataFrame([s_1,s_2,s_3,s_4])
print(pd_2)



