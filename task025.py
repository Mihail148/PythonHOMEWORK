# 25. Напишите программу, которая принимает 
# на вход строку, и отслеживает количество повторов каждого символа.

input_str = input("Введите строку: ")
characters_count = {}
for i in input_str:
    if i in characters_count:
        characters_count[i] += 1
    else:
        characters_count[i] = 1 
print(characters_count)           