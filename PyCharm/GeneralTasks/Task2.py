#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    c = int(input("Введите значение c: "))

    # Формула дискриминанта.
    D = (b ** 2) - (4 * a * c)

    if D > 0:
        print(f"Первый x = {(-b + (D ** (1 / 2))) / (2 * a)}\n"
              f"Второй x = {(-b - (D ** (1 / 2))) / (2 * a)}")
    elif D == 0:
        print(f"x = {-b / (2 * a)}")
    else:
        print("Отсутствуют действительные корни", file=sys.stderr)
        exit(1)