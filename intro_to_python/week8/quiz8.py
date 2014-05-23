## quiz 8 q3
s= set([1,2,3])
t= set([3,4,5])
print s, t
print

print s.union(t)
print s, t
print

print s.update(t)
print s, t
print

print s.intersection_update(s)
print s, t
print
print


## q8
def next(x):
    return (x ** 2 + 79) % 997

distinct=set([])
x = 1
distinct.add(x)
for i in range(1000):
    #print x
    x = next(x)
    distinct.add(x)

print len(distinct)
    
