a = float(input("Результат за первый день (км): "))
b = float(input("Желаемый результат (км): "))
day = 1
while a < b:
    a += a * 0.1
    day += 1
print(f"Достидение результата за {day} дней")