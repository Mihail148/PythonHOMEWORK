# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X. 
# Попробуйте использовать метод count(), а также решите задачу с 
# помощью своего алгоритма (без count). 
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.

# *Пример:*

# n = 5
# 1 2 3 4 5
# x = 3
# -> 1

n = abs(int(input('Введите количество элементов списка А: ')))
list_elem = input("Введите через пробел элементы списка: ").split()
list_num = list(map(int, list_elem))
if len(list_num) != n:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    x = int(input('Введите число X, которое необходимо найти в списке: '))
    count = 0
    for i in range(n):
        if list_num[i] == x:
            count += 1
    print(f'Число {x} встречается в списке A {count} раз')