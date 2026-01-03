def seq_sum(st,l,k):#st=start, l=list, k=sublist size
    s=0
    for i in range(st,k+st):
        s+=l[i]
    return s/k #avg

k=3 #k=sublist size
l=[1, 3, 2, 6, 2, 1]
x=3
c=0#count
len_l=len(l)
for i in range(0,len_l-k+1):
    avg=seq_sum(i,l,k)
    if(avg>=x):
        c+=1
print("Output:",c)