import pytest


# Создаем словарь при помощи dict(), получаем элемент словаря по ключу, проверяем что получили нужное значение

def test_dict_one():
    first_second_name = [['Patrick', 'Bonkowski'], ['Evgeniy', 'Elchugin'], ['Ksenia', 'Shkola'],
                         ['Anastasia', 'Grishina']]
    name_dict = dict(first_second_name)
    print(name_dict)
    name_dict['Sergey'] = 'Samborskiy'
    print(name_dict)
    assert 'Sergey' in name_dict


# Создаем словарь при помощи dict(), получаем элемент словаря по ключу,
# проверяем что получили нужное значение

def test_dict_two():
    second_first_name = [['Patrick', 'Bonkowski'], ['Evgeniy', 'Elchugin'], ['Ksenia', 'Shkola'],
                         ['Anastasia', 'Grishina'], ['Nastya', 'Sinegovskaya']]
    second_name_dict = dict(second_first_name)
    # print(second_name_dict)
    name = second_name_dict['Patrick']
    assert name == 'Bonkowski'


# Объединяем словари, проверяем, что записалось значения из первого словаря - записалось значение из второго словаря

def test_dict_three():
    dict1 = {'Elchugin': 1, 'Patrick': 'Poland'}
    dict2 = {'Ksuha': 'WhiteRussian', 'Sinegovskaya': 'Rubchik', 'Patrick': '777'}
    dict1.update(dict2)
    print(dict1)

    assert dict1['Patrick'] == '777'


# Объединяем словари, добавляем проверку на количество элементов обновленного списка

def test_dict_four():
    WebDevelopersDict = {'Evgeniy': 'Elchugin', 'Patrick': 'Bankowski', 'Daniel': 'Ghazi', 'Sergey': 'Samborskiy'}
    WebTestersDict = {'Ksenia': 'Shkola', 'Nastya': 'Sinegovskaya', 'Alina': 'Pravotorova', 'Evgeniy': 'Saganchi'}
    WebDevelopersDict.update(WebTestersDict)
    # print(WebDevelopersDict)
    lenDevelopersDict = len(WebDevelopersDict)
    assert lenDevelopersDict == 7


# Параметризация

log_data = {
    "WebDevPass": {
        "username": "Elchugin",
        "password": "Elchuginator1992"
    }, "WebTestPass": {
        "username": "Shkola",
        "password": "School1994!"
    }
}


@pytest.mark.parametrize(
    "data, value",
    [
        ({"WebDevPass": {"username": "Elchugin", "password": "Elchuginator1992"},
          "WebTestPass": {"username": "Shkola", "password": "School1994"}}, "correct value")
    ]
)
def test_dict_five(data, value):
    # Проверка на тип данных
    assert isinstance(data, dict)

    assert value == "correct value"
