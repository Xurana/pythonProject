text = input("Введите несколько слов: "). split()

for n, el in enumerate(text, 1):
    print(f'{n}) {el:.10}')