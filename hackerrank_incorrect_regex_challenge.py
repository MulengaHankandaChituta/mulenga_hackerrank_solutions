# hackerrank solution to detect valid regex

import re
import sys

def looks_invalid_by_quantifiers(p):
    # treat \x as escaped char; check first non-escaped char and adjacent quantifiers
    quant = set('*+?')
    n = len(p)
    # check first non escaped char
    i = 0
    while i < n:
        if p[i] == '\\':
            i += 2
            continue
        if p[i] in quant:
            return True
        break

    esc = False
    prev_q = False
    for ch in p:
        if esc:
            esc = False
            prev_q = False
            continue
        if ch == '\\':
            esc = True
            prev_q = False
            continue
        if ch in quant:
            if prev_q:
                return True
        else:
            prev_q = False
    return False
try:
    n = int(input().strip())
except:
    n = 0

for _ in range(n):
    pattern = input().strip('\n')
    # quick syntactic check to catch cases like '.*+' which pyhton's re may accept
    if looks_invalid_by_quantifiers(pattern):
        print(False)
        continue
    try:
        re.compile(pattern)
        print(True)
    except re.error:
        print(False)
                
                 
    
