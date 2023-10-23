#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

if __name__ == '__main__':
    c = int(input("Введите число от -8 до 8: "))
    result = ""

    if math.fabs(c) < 9:

        if c < 0:
            result = "Минус "
        if math.fabs(c) == 0:
            result += "ноль"
        elif math.fabs(c) == 1:
            result += "один"
        elif math.fabs(c) == 2:
            result += "два"
        elif math.fabs(c) == 3:
            result += "три"
        elif math.fabs(c) == 4:
            result += "четыре"
        elif math.fabs(c) == 5:
            result += "пять"
        elif math.fabs(c) == 6:
            result += "шесть"
        elif math.fabs(c) == 7:
            result += "семь"
        elif math.fabs(c) == 8:
            result += "восемь"
        print(result)
    else:
        print("Вы ввели неверное число", file=sys.stderr)
        exit(1)

