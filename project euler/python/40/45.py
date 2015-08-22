h=144
while True:
    if ((48*h**2-24*h+1)**0.5+1)%6==0:
        print 2*h-1,((48*h**2-24*h+1)**0.5+1)/6,h
        print h*(2*h-1)
        break
    h+=1
