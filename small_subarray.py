list=[2,3,1,2,4,3]
target=7
d=[]
for i in range(len(list)):
    sum=count=0#s=sum and c=count of subarray length and this count is stored in list d
    for j in range(i,len(list)):
        sum+=list[j]
        count+=1
        if(sum>target):
            break
        if(sum==target):
            d.append(count)
            break
print("Output", min(d))