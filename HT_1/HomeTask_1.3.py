n = input("Введите целое положительное число: ")
if n < '0':
    print("Введено отрицательное число")
else:
    print(f'{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}')
