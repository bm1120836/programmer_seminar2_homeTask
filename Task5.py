# Реализуйте алгоритм перемешивания списка

# задаю список из случайных чисел
import random
print('Введите число')
n = int(input())
lst = []
for i in range(n):
    num = random.randint(1, 100)
    lst.append(num)
print('Основной список')
print(lst)
# применяю функцию shuffle для перемешивания списка
random.shuffle(lst)
print('Перемешанный список')
print(lst)