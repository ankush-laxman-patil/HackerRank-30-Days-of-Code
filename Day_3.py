# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:29:51 2020

@author: ankuspat
"""
n=int(input())

a=1
def createlist(a,n):
    return list(range(a,n+1))

#for i in range(1,n):
#    print(i,end="")
#print()

def fizzBuzz(n):
    test=createlist(a,n)
    for i in test:
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0 and i%5 !=0:
            print("Fizz")
        elif i%3 !=0 and i%5 ==0:
            print("Buzz")
        elif i%3 !=0 or i%5 !=0:
            print(i)
    return;

fizzBuzz(n) 
