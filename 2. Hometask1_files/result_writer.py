import csv
import itertools
from csv import DictReader
from json import loads
from json import dumps


# with open('../data/data.csv', 'r') as file:
#    reader = csv.reader(file)
#    header = next(reader)
#    print(header)

#    for item in reader:
#        # print(item)
#        # print(dict(zip(header, item)))
#        print(dict(zip(header, item))['Title'])

    # используем контекстный менеджер для чтения csv файла

with open('./data/data.csv', 'r') as data_from_csv:
    reader = DictReader(data_from_csv)

    # Итерируемся по данным делая из них словари

    for row in reader:
        #print(row)
        print(row['Title'], row['Author'], row['Height'])
        # print(row['Title'])
        print(list(reader))
        csv1 = list(reader)

    # используем контекстный менеджер для чтения json файла
with open('./data/data1.json', 'r') as file:
    j = file.read()
    n = loads(j)
    for people in n:
        #rint(people)
        print(people['name'], people['gender'], people['address'])
    # print(type(n))
    # print(type(dumps(n)))

    # Используем контекстный менеджер для записи json в фаил

with open('newest_json.json', 'w') as newfile:
    s = dumps(row, indent=4)
    newfile.write(s)


def read_csv():
    # return dict_from_csv
    pass


def read_json():
    # return dict_from_json
    pass


def create_example_object(json_object, csv_object):
    # return user
    pass


def create_final_list():
    dict_from_csv = read_csv()
    dict_from_json = read_json()
    final = []
    for book, user in list(itertools.zip_longest(dict_from_csv, dict_from_json)):
        final.append(create_example_object(book, user))
    pass

    return final


def json_write(final):
    pass


def main():
    final_list = create_final_list()
    json_write(final_list)


main()
