def f(n):
    a=1
    for i in xrange(n):
        a*=n
        a%=(10**10)
    return a

g=lambda a,b: (a+b)%(10**10)
print reduce(g,[f(n) for n in xrange(1,1001)])
