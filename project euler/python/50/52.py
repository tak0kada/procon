def f():
    for i in xrange(1,100000000):
        s=set(str(i))
        for j in xrange(2,7):
            t=set(str(i*j))
            if s!=t: break
        else: return i
print f()
