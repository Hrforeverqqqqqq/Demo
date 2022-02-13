a=[1,2,3]
b=[2,3,4]
c=[]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            c.append(a[i])
        else:
            continue
print(c)


a1=set(a)
b1=set(b)
print(a1&b1)
