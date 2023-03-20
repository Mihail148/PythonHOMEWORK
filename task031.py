# Создайте список из случайных чисел. Найдите второй максимум.

import random

# input_list = [random.randint(1,100) for _ in range(10)]
input_list = list(set([10, 10, 4, 5, 6, 7, 8]))
print(input_list)
first_max = input_list[0]
second_max = input_list[1]

for i in input_list:
    if i > first_max:
        second_max = first_max
        first_max = i
    elif i > second_max and i != first_max:
        second_max = i
print(second_max)
