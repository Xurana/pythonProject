month = input("Введите номер месяца: ")
all_month = {"1": "зима", "2": "зима", "3": "весна", "4": "весна", "5": "весна", "6": "лето", "7": "лето", "8": "лето", "9": "осень", "10": "осень", "11": "осень", "12": "зима"}
while all_month.get(month) == None:
    print("Введенное значение не соответствует номеру месяца")
    month = input("Введите номер месяца: ")
print(f'Время года {all_month.get(month)}')
