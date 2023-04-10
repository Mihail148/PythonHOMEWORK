# Крестики нолики
# ввод по очереди начинают крестики 
# ввод координат клетки
# рисуем текущий статус

def get_game_status(fie):
    status_list = ["playing","win","draw"]
    for i in fie:
        if len(set(i)) == 1 and set(i).pop() != "-":
            return status_list[1]
        
    for i in range(3):
        if fie[0][i] == fie[1][i] == fie[2][i] != "-":
            return status_list[1]
    
    if fie[0][2] == fie[1][1] == fie[2][0] != "-":
        return status_list[1]
    
    if fie[0][0] == fie[1][1] == fie[2][2] != "-":
        return status_list[1]     
        
    for i in range(3):
        if "-" not in fie[i]:
            return status_list[0]
    return status_list[2]        

def set_mark(fie: list, mark: str, x: int, y= int):
    if fie[x][y] == "-":
        fie[x][y] = mark
        return True
    return False
            
field = [["-" for _ in range(3)] for _ in range(3)]

stop = False
while not stop:
    print(*field, sep="\n")
    print("ходит крестик")
    x, y = map(int, input().split())
    while not set_mark(field, "X", x, y):
        print("клетка занята")
        x, y = map(int, input().split())
    if get_game_status(field) == "win" or get_game_status(field) == "draw":
        stop = True
        print(get_game_status(field))
        continue
    print(*field, sep="\n")
    print("ходит нолик")
    x, y = map(int, input().split())
    while not set_mark(field, "0", x, y):
        print("клетка занята")
        x, y = map(int, input().split())
    if get_game_status(field) == "win" or get_game_status(field) == "draw":
        stop = True
        print(get_game_status(field))