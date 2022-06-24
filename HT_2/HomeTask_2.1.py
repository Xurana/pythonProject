list = [34, 12.5, 'cat', True, False, None,
        (7 + 4j), [8, 0], (4, 18), {5: "дом", 8: "дерево"},
        frozenset(), b'four', bytearray(b'one'),
        zip(*[(22, 15), (432, 12)]), TypeError]

for i, el in enumerate(list, 1):
    print(f' {i}) {el} - {type(el)}')

