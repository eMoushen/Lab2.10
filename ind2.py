#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def drive(**cars):
    for car, name in cars.items():
        print(f"{car}: {name}")


if __name__ == "__main__":
    drive(виды_машин=["седаны", "универсалы", "пикапы"],
          фирмы_машин=["mersedes", "jaguar", "nissan"])
