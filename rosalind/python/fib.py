#! /usr/bin/env/python3

n = int(input())
k = int(input())

a, b = 1, 0
for i in range(n-1):
    a, b = k * b, a + b

print(a+b)
