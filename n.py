
s=input()
l=[]
l.append(s[0])
maxi=0
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[j] not in l:
            l.append(s[j])
        else:
            break
    maxi=max(maxi,len(l))
    l=[]
    l.append(s[i])
print(maxi)
        
        
