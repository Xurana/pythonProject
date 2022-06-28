def my_div():
        try:
                num_1 = float(input("Введите первое число: "))
                num_2 = float(input("Введите второе число: "))
                div = num_1 / num_2
        except ZeroDivisionError:
                return "Делить на ноль нельзя!!!"
        except ValueError:
                return "Value Error"
        return round(div, 4)

print(my_div())
