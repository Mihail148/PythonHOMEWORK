# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

def cross_arrays(input_arr1, input_arr2):
    second_set = set(input_arr2)
    result = []
    for i in input_arr1:
        if i not in second_set:
            result.append(i)
    return result        

len_first_array = int(input("Введите длину первого массива: "))
first_array = []
for i in range(len_first_array):
    first_array.append(input(f"Введите {i + 1}-й элемент первого массива: "))

len_second_array = int(input("Введите длину второго массива: "))
second_array = []
for i in range(len_second_array):
    second_array.append(input(f"Введите {i + 1}-й элемент второго массива: "))    

print(cross_arrays(first_array, second_array))    