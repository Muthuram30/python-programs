s="abc de fg hij"
c=0
max=0
for i in s:
    if i!=' ':
        c+=1
    else:
        if(c>max):
            max=c
        c=0
print("Output:", c)
#there is a bug if s="abc  start  ", c=0