def int_func():
    for word in input("Введите через пробел слова, состоящие из латинских букв нижнего регистра: ").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f'{word} - Вводите только маленькие латинские буквы')

int_func()