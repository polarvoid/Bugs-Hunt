#!/usr/bin/env python3

# A program to print the number at the ninth index of the fibonacci series
# 
# Expected output: 34

def fibo(n):
    if n<0:
        print("Incorrect input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fibo(n-1) + fibo(n-2)
 
print(fibo(9))