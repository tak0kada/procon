def p(n):
    return (3*n-1)*n/2

def isP(n):
    if (1+(1+24*n)**0.5)%6==0: return 1
    else: return 0

i,I=1,2.0
while True:
    for d in range(1,int(0.415*i)+1):
        j=(I/d-3*d+1)/6
        if j>i and j%1==0 and isP(p(j)-p(i)):
            print i,j,d
            print "D=|p(i)-p(j)|=",p(j)-p(i)
            raise IOError
    I+=6*i+2
    i+=1
