#!/usr/bin/python3
print("Enter the first number: ")
n1 = int(input())
print("Enter the second number: ")
n2 =int(input())
print(n1, "x",  n2)
print(n1 * n2)
product = n1 * n2
if product ==0:
    print("The result is positive and negative.")
if product >0:
    print("The result is positive.")
if product <0:
    print("The result is negative.")