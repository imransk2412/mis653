# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:17:24 2024

@author: skimr
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = int(input("Enter the number: "))
prime_check = is_prime(number)
print(f"Is {number} prime? {prime_check}")