#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = int(input("Введите значение в фунтах "))

    print("Фунты\tКилограммы")
    print("--------")

    for pounds in range(1, a + 1):
        kilograms = pounds * 400 / 1000
        print(f"{pounds}\t{kilograms:.1f}")
