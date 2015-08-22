def isPrime(n,L):
    if n==1: return 0
    else:
        for i in L:
            if n%i==0: return 0
        else: return 1

primeList=[2]
for i in xrange(10000):
    if isPrime(i,primeList): primeList.append(i)
print primeList

for p in primeList:
    index=primeList.index(p)
    for cod in xrange(primeList[index-1]+1,p):
        if cod%2==1:
            if not isPrime(cod,primeList):
                for i in xrange(index):
                    if ((cod-primeList[i])/2)**0.5%1==0: break
                else: print cod
