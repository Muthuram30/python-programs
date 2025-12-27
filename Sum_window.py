def seq_sum(st,l,k):#st=start, l=list, k=sublist size
    s=0
    for i in range(st,k+st):
        s+=l[i]
    return s

k=3
l=[2,1,5,1,3,2]
s=0#output sum for max sublist
len_l=len(l)
for i in range(0,len_l-k+1):
    sum=seq_sum(i,l,k)
    if(sum>s):
        s=sum
print("Output:",s)