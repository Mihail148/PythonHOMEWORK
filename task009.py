# 9. По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

number = int(input("Введите число N: "))
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print(factorial)    