from itertools import permutations

L,ans=[2,3,5,7,11,13,17],0
for n in permutations(range(10)):
    s="".join(map(str,n))
    for i in xrange(1,8):
        if int(s[i:i+3])%L[i-1]!=0: break
    else: ans+=int(s)
print ans
