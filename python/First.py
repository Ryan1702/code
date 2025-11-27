l=[]
for i in range(5):
    print("Temperature",i+1,sep="",end=":")
    l.append(int(input()))
s=0
for i in range(5):
    s+=l[i]
print(s/5)