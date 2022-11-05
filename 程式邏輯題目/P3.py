#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
#P3
"""
QA部門今天舉辦團康活動，有n個人團成一圈，順序排號。
從第一個人開始報數(從1到3報數)，凡報到3的人退出圈子。
請利用一段程式計算出，最後留下的那位同事，是所以同事裡面的第幾順位?
"""

if __name__ == '__main__':
    n = int(input("請輸入人數:"))
    Tmplist = list(range(1,n+1))
    count = 0
    while True:
        if len(Tmplist) == 1:
            break
        else:
            count += 1
            pop = Tmplist[0]
            Tmplist.pop(0)
            if count == 3:
                count = 0
                continue
            else:
                Tmplist.append(pop)
    print("輸出：",Tmplist)


