from json import loads, dumps


# Чтение из json файла (доб функцию)
# with open('../data/data1.json', 'r') as file:
#     j = file.read()
#     n = loads(j)
#     print(n)
#     #print(type(n))


    # Итерируем
"""    for people in n:
        #print(people)
        print(people['name'], people['gender'], people['address'])"""


    # print(type(n))
    # print(type(dumps(n)))

    # Запись в новый json фаил
# with open('first_json.json', 'w', encoding='utf-8') as first:
#     abc = dumps(n, indent=4)
#     first.write(abc)


def test_read_js():
    # return dict_from_json
    with open('../data/data1.json', 'r') as file:
        j = file.read()
        peoples = loads(j)
        # print(peoples)
        # print(type(n))
    return peoples
abc = test_read_js()

print(abc)
