# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

input_list = []
list_len = int(input("Введите кол-во элементов списка: "))
for _ in range(list_len):
    input_list.append(int(input("Введите число: ")))
print(input_list)

input_set = set(input_list)

print(f"Различных чисел {len(input_set)}")    