spisok = list(input("Введите элементы списка: "))
print(spisok)
for el in range(0, len(spisok) - 1, 2):
    spisok[el], spisok[el + 1] = spisok[el + 1], spisok[el]
print(spisok)