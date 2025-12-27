s="aabbccdde"
l=len(s)
arr=list(s)#due to mutability
i=1
while(i<l):#while prefered due to non fixed length of l
    if(arr[i]==arr[i-1]):
        arr.pop(i)
        l-=1
    else:
        i+=1
print("Output:",l)