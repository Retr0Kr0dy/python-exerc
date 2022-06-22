try:
    import sys
    try:
        xv =sys.argv[1]
    except:
        xv = "1"
    def spell(xv):
        xv = xv + "!"
        Lxv = []
        for xx in xv:
            Lxv.append(xx)
        Lresp = []
        def reading():
            Ltmp = []
            while len(Lxv) >= 2:
                av = Lxv[0]
                if av == Lxv[1]:
                    Ltmp.append(Lxv[1])
                    Lxv.pop(1)
                else:
                    yv = 0
                    yv = len(Ltmp) + 1
                    Lresp.append(yv)
                    try:
                        Lresp.append(Lxv[0])
                    except:
                        Lresp.append("1")
                    Lxv.pop(0)
                    Ltmp=[]
        reading()
        xv = ''.join(str(e) for e in Lresp)
        print("")
        input(xv)
        spell(xv)
    spell(xv)
except:
    print("""\n\n\n  Usage  ;  read-and-spell.py (starting with 1) |or| read-and-spell.py <integer> (starting with int)
    
    press enter to continue printing result""")
