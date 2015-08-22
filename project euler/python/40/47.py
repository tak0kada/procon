from sympy import factorint

c,i=0,1
while True:
    if len(factorint(i))==4: c+=1
    else: c=0

    if c==4:
        print i-3
        break
    i+=1
