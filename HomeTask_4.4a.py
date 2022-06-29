from random import randint


a_list = [randint(-20, 20) for tr in range(20)]
sp_lst = [el for el in a_list if a_list.count(el) == 1]
print(f"Источник - {a_list} \nСписок без повторов - {sp_lst}")