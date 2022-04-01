# Author: Quentin Bergeron
# File: practice.py
# Date started: 28 September 2021
# Purpose: to create a calculator to help solve simple math problems.

def add(a,b):
    result=a+b
    print("a+b", result)

def sub(a,b):
    result=a-b
    print("a-b", result)

def mul(a,b):
    result=a*b
    print("a*b", result)

def div(a,b):
    result=a/b
    print("a//b", result)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
op=input("Enter the operator: ")

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="//":
    div(a,b)

else:
    print("Invalid5")

