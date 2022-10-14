# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math
print('Введите число')
n = int(input())
lst = [1]
i = 2
while i <= n:
    num = math.factorial(i)
    lst.append(num)
    i = i + 1
print(lst)