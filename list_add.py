def list_len(a):
    count=0
    for i in a:
        count+=1
    return count

m=eval(input("Enter the list:"))
dup_list=[]
l=list_len(m)# calling a user defined func for calc length
for i in range(0,l):
    if(i<l-1):
        dup_list.append(m[i]+m[i+1])
    else:
        dup_list.append(m[i])
print("The required list is", dup_list)