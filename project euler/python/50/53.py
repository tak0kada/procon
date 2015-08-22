#53
def fact(n): return reduce(lambda a,b: a*b, [1,]+range(1,n+1))
def comb(n,r): return fact(n)/fact(r)/fact(n-r)

cnt=0
for n in xrange(1,101):
    for r in xrange(0,n//2):
        if comb(n,r)>1000000:
            cnt+=(n+1-2*r)
            break
print cnt
