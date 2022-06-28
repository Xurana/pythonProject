def my_func (num_1, num_2, num_3):
        try:
                my_str = list(map(float, (num_1, num_2, num_3)))
                my_str.remove(min(my_str))
                return sum(my_str)
        except (TypeError, ValueError):
                return "Вводите только цифры!"

print(my_func(input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: ")))