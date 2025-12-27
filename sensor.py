def count(a):
    c=0
    for i in a:
        if(i[0]=='#'):
            continue
        else:
            c+=1
    print("count is:", c)
def min_max_dist(d):
    print("minimum=",min(d))
    print("maximum=",max(d))

def wall_approach(d,l):
    c=0
    for i in range(1,l-1):
        if(d[i-1]>d[i] and d[i]<d[i+1]):
            c+=1
    print("Wall approach:",c)

with open("sensor_data.txt") as f:# to eliminate the use of f.close use with open
    a = f.read().splitlines('\n')#exludes the \n charcter so it is prefered over readlines
    count(a)
    d=a.copy()#shallow copy is created as there is no use of innerlist modification here
    l=len(d)
    i=0
    while(i<l):
        if(d[i].startswith('#')):
            d.pop(i)
            l-=1
        else:
            d[i]=float(d[i])
            i+=1#index_count
    min_max_dist(d)
    wall_approach(d,l)