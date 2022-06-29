from  itertools import  count
from math import factorial


def fact_cr():
    for el in count(1):
        yield factorial(el)


x = 0
for i in fact_cr():
    if x < 15:
        x += 1
        print(f"Факториал {x} = {i}")
    else:
        break