month = int(input("Введите номер месяца: "))
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if winter.count(month) > 0:
    print('Это зима')
elif spring.count(month) > 0:
    print("Месяц весенний")
elif summer.count(month) > 0:
    print("Это лето")
elif autumn.count(month) > 0:
    print("Осень")
else:
    print("Нету таких месяцов")