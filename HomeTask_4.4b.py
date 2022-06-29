from random import randint


a_list = [randint(-20, 20) for tr in range(20)]
th_dict = {i: 0 for i in a_list}

for i in a_list:
    th_dict[i] += 1

print(f"Исходный список - {a_list}")
print("Список без повторов -", [i for i in th_dict if th_dict[i] == 1])