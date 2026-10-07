def letterize(num):
    if not(0 <= num <= 99): raise ValueError

    digits = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять"}
    uniques = {0: "ноль", 1: "десять", 4: "сорок", 9: "девяносто"}

    if num//10 == 1 and num%10 != 0: return(f"{digits[num%10][:-1]}{'н' if num%10 == 1 else 'е' if num%10 == 2 \
                                                                    else 'и' if num%10 == 3 else ''}надцать")
    elif num//10 == 0 and num%10 != 0: return(f"{digits[num%10]}")
    elif num//10 in list(uniques.keys()): return(f"{uniques[num//10]} {digits[num%10] if num%10 != 0 else ''}")
    else: return(f"{digits[num//10]}{'дцать' if 2 <= num//10 <= 3 else 'десят' if 5 <= num//10 <= 8 else ''} {digits[num%10] \
                                                                                                            if num%10 != 0 else ''}")

try:
    print(letterize(int(input("Введите целое число от 0 до 99: "))))
except ValueError:
    print("Неправильный ввод")

# for i in range(0, 100):
#     letterize(i)
