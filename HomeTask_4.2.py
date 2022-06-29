from random import randint


num_list = [randint(0, 1000) for tr in range(0, randint(1,25))]
more_num = [num for i, num in enumerate(num_list[1:]) if num > num_list[i]]

print(num_list)
print(more_num)