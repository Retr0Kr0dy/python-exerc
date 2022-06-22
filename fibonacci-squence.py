try:
    import sys
    xv="01"
    inp=sys.argv[1]
    if inp == "0":
        print("0")
    elif inp == "1":
        print("1")
    else:
        x=0
        y=1
        def Fibo(x,y):
            z = x + y
            return x,y,z
        def CountingFibo(x,y,xv):
            for i in range(1,int(inp)):
                x, y, z = Fibo(x,y)
                x=y
                y=z
                xv = xv + str(z)
            return xv, str(z)
        aa,bb=CountingFibo(x,y,xv)
        print(bb)
except:
    print("\n ¬ Usage  ;  fibancci.py <iteration>       exemple :: fibancci.py  14  will return  377\n")
