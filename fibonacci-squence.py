#!/usr/bin/env python3
from argparse import ArgumentParser
from sys import exit

"""
Actually doing math.
"""
def my_fibo(stop) -> list:
    ret = []
    x,y,c   = 3*[0,]
    y       = y+1

    while (c <= stop):
        ret.append((x+y))
        x  = y
        y  = ret[len(ret)-1]
        c  = c+1

    return ret

"""
Pasing arguments.
"""
def parser() -> tuple:
    p = ArgumentParser()
    p.add_argument( "value", nargs="?", help="Input value.")
    p.add_argument( "--range", "-r",  help="Print range from 0 to value.")

    return p.parse_args()

"""
Main func, handling other funcs.
"""
def main() -> int:
    args = parser()
    if args.value:
        print(my_fibo(int(args.value))[int(args.value)])
    elif args.range:
        for i in (my_fibo(int(args.range))): print(i)
    else:
        print("[ERROR] - bad usage !!!\n\ntry\n\tfibo.py -r 12\nor\n\tfibo.py 12")
    return 0

if __name__ == "__main__":
    exit(main())
