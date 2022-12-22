#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def jump(**kwargs):
    summa = 0
    n = len(kwargs)
    max = kwargs["Иванов"]
    for kw in kwargs:
        summa = summa + kwargs[kw]
        if kwargs[kw] > max:
            max = kwargs[kw]
    print("Самый длинный прыжок:", max)
    print("Средняя длина прыжка у участников = ", summa / n)


if __name__ == "__main__":
    jump(
        Иванов=5.8,
        Козлов=6.1,
        Ефремов=3.4,
        Ефимов=4.6
    )
