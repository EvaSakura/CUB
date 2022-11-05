#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
#P1
"""
國泰補習班中，有五位學生期中考的成績分別為[53,64,75,19,92]，
但是老師在輸入成績的時候看反了，把五位學生的成績改成了[35,46,57,91,29]，
請用一個函數來將學生的成績修正。
"""

if __name__ == '__main__':
    #TmpList = list(map(int, input().split()))
    InputData = [35,46,57,91,29]
    print ("輸入：",InputData)
    for i in range(len(InputData)):
        tmp = str(InputData[i])
        InputData[i] = int(tmp[-1::-1])
    print ("輸出：",InputData)



