# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:22:59 2024

@author: skimr
"""

def char_count(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1  
        else:
            count[char] = 1  
    return count

result = char_count("hello world")
print(result)
