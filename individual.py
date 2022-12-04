#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multip(*args):
    amin = 0
    amax = 0
    maxim = 0
    proiz = 1
    if args:
        for i in args:
            if i > maxim:
                maxim = i
                amax = args.index(i)

        mini = args[0]
        for i in args:
            if i < mini:
                mini = i
                amin = args.index(i)

        for i in args[amin+1:amax:]:
            proiz *= i
        return 'Произведение =', proiz

    else:
        return None


if __name__ == "__main__":
    print(multip(10, 150, 5, 400, 13, 555))