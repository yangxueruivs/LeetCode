# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 18:57:26 2016

@author: Yxr
"""

#N-Queens
def conflict(positions, new):
    for i in range(len(positions)):
        if abs(int(positions[i]) - new) in (0, len(positions)-i):
            return True
    return False
    
def conflict1(positions, new):
    for i in range(len(positions)):
        if abs(positions[i] - new) in (0, len(positions)-i):
            return True
    return False
   
def Queens(n, pos):
    for i in range(n):
        if not conflict1(pos, i):
            print i
            if len(pos) == n-1:
                yield (i,)
            else:
                for j in Queens(n, pos + (i,)):
                    print j
                    yield (i,) + j
                    
def NQueens(n, pos):
    for i in range(n):
        if not conflict(pos, i):
            if len(pos) == n-1:
                yield list(str(i))
            else:
                for j in NQueens(n, pos + list(str(i))):
                    yield list(str(i)) + j
                    
def printQueens(result, n):
    for i in range(len(result)):
        for j in range(n):
            temp = result[i][j]
            result[i][j] = ""
            for k in range(int(temp)):
                result[i][j] += '.'
            result[i][j] += 'Q'
            for l in range(n-int(temp)-1):
                result[i][j] += '.'
    print result