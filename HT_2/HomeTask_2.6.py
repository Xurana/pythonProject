items = []
products = {"название": "", "цена": "", "количество": "","ед. изм.": ""}
analytics = {"название": [], "цена": [], "количество": [],"ед. изм.": []}
numb = 0
while True:
    if input("Введите exit для выхода из программы, enter - для продолжения").upper() == "exit":
        break
    numb += 1
    copy_prod = products.copy()
    for p in products:
        pro = input(f"Введите значение для '{p}': ")
        copy_prod[p] = int(pro) if p in "цена количество" and pro.isdigit() else pro
        analytics[p].append(copy_prod[p])
    items.append((numb, copy_prod))
    print(f'\n Структура товаров\n{items}')
    print(f'\nТекущая аналитика:\n{"=" * 30} ')
    for key, value in analytics.items():
        print(f'{key}: {value}')
    print("=" * 30)

