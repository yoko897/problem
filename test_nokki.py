#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def func(x):
    # 2進数に変換
    t = bin(x)[2:]
    ans = ''
    for i in t:
        print(i)
        if i == '0':
            ans += i
        else:
            ans += 2
    print(ans)

func(3)