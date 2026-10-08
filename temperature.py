def new_scale(x):
    temp, scale = int(x[:-1]), x[-1]
    if not(scale.lower() in ["f", "c"]): return("Неправильная шкала")
    if scale.lower() == "c": return(f"{int(temp * 1.8 + 32)}F")
    else: return(f"{int((temp - 32) / 1.8)}C")

try:
    print(new_scale(input("Введите температуру в градусах цельсия/фаренгейта: ")))
except ValueError:
    print("Неправильный ввод")
