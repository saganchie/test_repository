import csv
from csv import DictReader
import json
from json import dumps

# with open('../data/data.csv', 'r') as file:
#    reader = csv.reader(file)
#    header = next(reader)
#    print(header)

#    for item in reader:
#        # print(item)
#        # print(dict(zip(header, item)))
#        print(dict(zip(header, item))['Title'])

# Чтение из csv файла

# with open('../data/data.csv') as k:
#     reader = DictReader(k)
#
#     for row in reader:
#         print(row)

with open("../data/data.csv") as books:
    reader = DictReader(books)

    for row in reader:
        print(row)



    # print(list(reader))
    # csv1 = list(reader)

    # Итерируемся по данным делая из них словари
    # for row in reader:
    #     print(row)

    #     print(row['Title'], row['Author'], row['Height'])
    #     # print(row['Title'])

##### Попытки
# with open('second_json_from_cvs.json', 'w') as second:
#     new_variable = dumps(reader, indent=4)
#     second.write(new_variable)

# with open('third_json.json', 'w') as third:
#      json.dump(reader, third).

# Последний удачный

# with open("1first1_json.json", 'w') as file:
#     s = dumps(csv2, indent=4)
#     file.write(s)
