from sys import argv


import sys
xv="01"
inp=sys.argv[1]
if inp == "r":
    print(inp)
    r = sys.argv[2]
    x=0
    y=1
    def Fibo(x,y):
        z = x + y
        return x,y,z
    def CountingFibo(x,y,xv):
        for i in range(1,int(r)):
            x, y, z = Fibo(x,y)
            x=y
            y=z
            xv = xv + str(z)
            print("i =",i,"   \t\t\t\t",str(z))
    CountingFibo(x,y,xv)
elif inp == "0":
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
