def list_len(a):
    c=0
    for i in a:
        c+=1
    return c

m=eval(input("Enter the list:"))
n=[]
l=list_len(m)# calling a user defined func for calc length
for i in range(0,l):
    if(i<l-1):
        n.append(m[i]+m[i+1])
    else:
        n.append(m[i])
print("The required list is", n)