# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, 
# а другой для тещи. Понятно, что для себя
# нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке 
# каждое. Здесь каждое число – это масса соответствующего арбуза. 
# Все числа натуральные и не превышают 30000.

quantity = int(input("Введите кол-во арбузов: "))
max_weight = 0
min_weight = 0
for i in range(quantity):
    current_weight = int(input("Введите вес арбузов: "))
    while current_weight <= 0 or current_weight > 30000:
        print("Такой арбуз не унести")
        current_weight = int(input("Введите вес арбузов: "))
    if i == 0:
        min_weight = current_weight
        max_weight = current_weight
    if i != 0:
        if current_weight > max_weight and current_weight < 30000:
            max_weight = current_weight
        if current_weight < min_weight and current_weight > 0:
            min_weight = current_weight
print(f"Арбуз для себя {max_weight} и арбуз для тещи {min_weight}")                
        
