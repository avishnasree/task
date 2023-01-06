# 4.Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square.

# def find_even():
#     list=[]
#     for i in range(1000,10000):
#         sum=0
#         i=str(i)
#         for j in i:
#             j=int(j)
#             sum=sum+j
#         if sum%2==1:
#             list.append(i)
#     print(list)
#     for k in range(i)
#
# find_even()


even_square_numbers = []

for num in range(1000, 10000):
    num_string = str(num)
    all_even = True
    for digit in num_string:
        if int(digit) % 2 != 0:
            all_even = False
            break
    if all_even:
        sqrt = int(num ** 0.5)
        if sqrt ** 2 == num:
            even_square_numbers.append(num)
print(even_square_numbers)