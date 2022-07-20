
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
s={}
for i in d1:
    if  i in d2:
        s[i]=d1[i]+d2[i]
    else:
        s[i]=d1[i]
for j in d2:
    if j in d1:
        s[j]=d2[j]+d1[j]
    else:
        s[j]=d2[j]
print(s)
    