rating = [9, 7, 2, 4, 1, 3, 2]
numb = ""

while numb != "ex":
    i = 0
    numb = input("Введите натуральное число либо ex для завершения ")

    if numb.isdigit():
        for el in rating:
            if int(numb) <= el:
                i += 1
            else:
                break
        rating.insert(i, int(numb))
    print(rating)
