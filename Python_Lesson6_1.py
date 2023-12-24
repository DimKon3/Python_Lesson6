num = int(input("Введите число: "))
count = 0

for i in range(1, num+1):
    if num % i == 0:
        count += 1

print(f"Количество делителей числа {num} равно {count}")