def count(l,c):
    s=0
    for i in l:
        if (i==c):
            s+=1
    return s
l=[0,1,0,0,1,1,0]
z_c=count(l,0)#counts the no of zeroes
o_c=count(l,1)#counts the no of ones
r=min(z_c,o_c)*2
print("Output:",r)
