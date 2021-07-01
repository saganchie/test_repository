import json
import csv
from itertools import zip_longest


def test_read_csv():
    # return_dict_from_csv
    with open("./data/data.csv", 'r') as books:  # менеджер контекста
        cin = csv.DictReader(books)
        villi = [row for row in cin]
    return villi


def test_read_json():
    # return dict_from_json
    with open('./data/data1.json', 'r') as file:  # менеджер контекста
        j = file.read()
        peoples = json.loads(j)
    return peoples


def create_example_object(book, user):
    if not user:
        return
    user_with_book = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "books": [],
    }
    if book:
        book_with_people = {
            "title": book["Title"],
            "author": book["Author"],
            "height": book["Height"],
        }
        user_with_book['books'].append(book_with_people)
    return user_with_book


def test_create_final_list():
    dict_from_csv = test_read_csv()
    dict_from_json = test_read_json()
    final = []
    for book, user in zip_longest(dict_from_csv, dict_from_json):
        final_example = create_example_object(book, user)
        # если в finalexample есть none. то не аппендить его в final
        if final_example:
            final.append(final_example)
    return final


with open("./output.json", "w+") as output:
    output.write(
        json.dumps(test_create_final_list())
    )
