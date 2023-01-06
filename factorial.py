# 1. Write a program to find the factorial of a number.

n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("The factorial of 5 is : ", end="")
print(fact)
