result = []

stop = False
first_letter = input("Введите символ: ")
while not stop:
    input_str = input("Введите строку: ")
    if input_str == "ВЕЧЕР":
        stop = True
    part_list = input_str.split(first_letter)
    if len(part_list) > 1:
        result.append(part_list[1])

print(*set(result), sep="\n")
           