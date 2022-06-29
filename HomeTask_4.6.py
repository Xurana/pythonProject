from itertools import islice, count, cycle

def func(st_el, stop_el, num_str):
    try:
        st_el, stop_el, num_str = int(st_el), int(stop_el), int(num_str)
        list = [el for el in islice(count(),st_el, stop_el + 1)]
        r_list = iter(el for el in cycle(list))
        rep_list = [next(r_list) for x in range(num_str)]
        print(list)
        return rep_list
    except ValueError:
        return "Value Error"
    except TypeError:
        return "Type Error"

print(func(input("Начинать с числа -"), input("продолжать до -"), input("Количество повторений -")))