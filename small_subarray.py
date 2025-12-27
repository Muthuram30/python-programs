l=[2,3,1,2,4,3]
t=7
d=[]
for i in range(len(l)):
    s=c=0#s=sum and c=count of subarray length and this count is stored in list d
    for j in range(i,len(l)):
        s+=l[j]
        c+=1
        if(s>t):
            break
        if(s==t):
            d.append(c)
            break
print("Output", min(d))