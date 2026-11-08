def units(a):
    cost = 0
    v=0
    zz=0
    h=0
    if a>=0:
        if a<=100:
            cost = 2
            v=a*cost
        elif a<=200 and a>100:
            cost = 3
            v=a*cost
        elif a<=300 and a>200:
            cost = 5
            v=a*cost
        elif a>300:
            cost = 7 
            v=a*cost
    else:
        print("invali units")
        return a


    if v<50:
        v=50
        print("the fixed bill is",v)
        return v
    elif v >50 and v<2000:
        print("the bill is :", v )
        return v
    elif v>2000:
        h=v/5
        zz=v-h
        print("the bill is after dicount",zz)
        return zz
    
units(24)
units(100)
units(150)
units(250)
units(400)