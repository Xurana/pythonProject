t = int(input("Введите время в секундах: "))
if t >= 0:
    hh = t//3600
    mm = (t%3600)//60
    ss = (t%3600)%60
    print('%02d:%02d:%02d' %(hh, mm, ss))
else:
    print("Неверное значение")