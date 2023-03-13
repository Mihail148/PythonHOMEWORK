# 11. Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое
# число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

number = int(input("Введите натуральное число A: "))
f1 = 0
f2 = 1
temp_fibonachi = f1 + f2
index = 3
while temp_fibonachi < number:
    f1 = f2
    f2 = temp_fibonachi
    temp_fibonachi = f1 + f2
    index += 1
if temp_fibonachi == number:
    print(index)
else:        
    print(-1)    
