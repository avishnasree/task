# 7. Write a program to generate all factors of a number. [use while loop]

number = int(input("Enter a number "))

for i in range(1,number+1):
    if number % i == 0:
        print(i)