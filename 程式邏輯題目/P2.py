#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
#P2
"""
國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間，
文字為"Hello welcome to Cathay 60th year anniversary"，
請寫一個程式計算每個字母(大小寫視為同個字母)出現次數。
"""

if __name__ == '__main__':
    #tmpstr = "Hello welcome to Cathay 60th year anniversary".lower()
    #print ({a:tmpstr.count(a) for a in set(tmpstr.replace(' ',''))})

    tmpstr = input().upper()
    tmparray = tmpstr.split(" ")
    #print("String Len:",len(tmpstr))
    print("輸出:")
    Ans = [0]*123
    for i in range(len(tmpstr)):
        Ans[ord(tmpstr[i])] = Ans[ord(tmpstr[i])] + 1

    for i in range(48,123):#搜尋並計算數字大小寫英文
        if Ans[i] != 0:
            print(chr(i),"-", Ans[i])

