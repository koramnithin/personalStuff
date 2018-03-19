a = [1,10,8,12,11,13]
s = 0
l = []
r = []
for i in range(len(a)):
    if i%2 != 0:
        l.append(a[i])
    else:
        r.append(a[i])
l.sort()
r.sort()

for j in range(1,len(l)):
    if l[j-1]<l[j]<r[j-1]:
        s+=1
print(s)
