def count(list,num):
    s=0
    for i in list:
        if (i==num):
            s+=1
    return s
l=[0,1,0,0,1,1,0]
zero_count=count(l,0)#counts the no of zeroes
one_count=count(l,1)#counts the no of ones
r=min(zero_count,one_count)*2
print("Output:",r)
