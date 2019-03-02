a = ['hello','world','1','2']
l1=a[0::2]
l2=a[1::2]
print(l1) #分片(起点：终点：步长）
print(l2)
print(dict(zip(l1,l2)))