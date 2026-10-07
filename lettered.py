def letterize(num):
    if not(0 <= num <= 99): raise ValueError

    ones = "ноль один два три четыре пять шесть семь восемь девять".split()
    teens = "десять одиннадцать двенадцать тринадцать четырнадцать пятнадцать шестнадцать семнадцать восемнадцать девятнадцать".split()
    tens = "- - двадцать тридцать сорок пятьдесят шестьдесят семьдесят восемьдесят девяносто".split()

    if num < 10: return ones[num % 10]
    if num < 20: return teens[num - 10]
    else: return(f"{tens[num // 10]} {ones[num % 10] if num % 10 != 0 else ''}")

try:
    print(letterize(int(input("Введите целое число от 0 до 99: "))))
except ValueError:
    print("Неправильный ввод")

# for i in range(0, 100):
#     print(letterize(i))

