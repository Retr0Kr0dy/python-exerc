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
    print("Lresp = ", xv)
    input("\n  ...  ...  ...  ...  ...  ...  ...")
    spell(xv)
spell(xv)
