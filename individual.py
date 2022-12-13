#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sump(*args):
    amin = 0
    amax = 0
    if args:
        for index, i in enumerate(args):
            if i > args[amax]:
                amax = index
            elif i < args[amin]:
                amin = index

        return sum([i for i in args[amin+1:amax:]])

    else:
        return None


if __name__ == "__main__":
    print(sump())
    print(sump(3, 5, 7, 12, 13, 10))
