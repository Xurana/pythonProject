def my_func(x, y):
        try:
                x, y = float(x), int(y)
                if x > 0 and y < 0:
                        res = 1
                        for i in range(abs(y)):
                                res /= x
                        return f"Результат возведения чила x в степень y равно {round(res, 6)}"
                else:
                        return "Не выполнено условие задания: x > 0, y < 0"
        except ValueError:
                    return "Вводите числа!"

numb_1 = input("Введите действительное положительное число x = ")
numb_2 = input("Введите целое отрицательное число y = ")

print(my_func(numb_1, numb_2))