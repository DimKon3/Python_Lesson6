count = int(input("Сколько чисел будем вводить: "))
kol_zerro = 0
for i in range(count):
    num = int(input("Введите очередное число:"))
    if num == 0:
        kol_zerro += 1

print(f"Количество чисел равных нулю - {kol_zerro}")