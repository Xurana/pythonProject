from functools import reduce

def list(el1, el2):
    return el1 * el2


th_list = [el for el in range(100, 1001, 2)]
print(f'Список\n{th_list}\nРезультат перемножения\n{reduce(list, th_list)}')