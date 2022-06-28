def  n_sum():
    sm = 0
    while True:
        error = False
        list = input("Введите числа через пробел, либо q - для выхода ").split()
        for num in list:
            if num.lower() == 'q':
                return sm
            else:
                try:
                    sm += int(num)
                except ValueError:
                    error = True
        if error:
            print("Некорректные значения!")
        print(f"Сумма чисел {sm}")

print(n_sum())