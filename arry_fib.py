a=[3,3,3,7,7,7,10,10,10]
b=[]
b.append(a[0])

for i in range(0,len(a)-1):
    value_to_append=b[i]+a[i+1]
    b.append(value_to_append)
print(b)