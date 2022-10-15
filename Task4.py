# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from math import prod


with open('1.txt', 'r') as my_file:
    data = my_file.read()
lst = data.split()
result_lst = [int(item) for item in lst]
print(result_lst)
print(prod(result_lst))
    