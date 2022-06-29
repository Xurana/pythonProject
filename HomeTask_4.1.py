from sys import argv


def zp():
    try:
        time, rate, bonus = map(float,argv[1:])
        print(f"Зарплата - {(time * rate + bonus) * 0.87}")
    except ValueError:
        print("Вводите 3 чила.")

zp()