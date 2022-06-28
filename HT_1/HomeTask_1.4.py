num = int(input("Введите целое положительное число: "))
l = 0
while num > 0:
    last_n = num % 10
    if last_n > l:
        l = last_n
        if l == 9:
            break
    num //= 10
print(f'Самая большая цифра в числе {l}')
