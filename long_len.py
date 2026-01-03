def rstrip_spaces(s):
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    return s[:i+1]

a="abc de fg hij  "
s=rstrip_spaces(a)
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
