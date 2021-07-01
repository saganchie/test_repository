import pytest


# Проверка на то, что первый элемент списка == 'Monday'

def test_list_one():
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    assert weekdays[0] == 'Monday'


# Проверка на то, что второй элемент списка != 'Monday'

def test_list_two():
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    assert weekdays[1] != 'Monday'


# Проверяем значение элемента в списке по его значению

def test_list_three():
    mexicans = ['Marco', 'Garsia', 'Gumo', 'Gonsales', 'Migel']
    assert mexicans.index('Gumo') != 3


# Проверяем, что элемент встречается в списке 1 раз(Проверяем наличие элемента в списке с помощью оператора in)

def test_list_four():
    mexicans = ['Marco', 'Garsia', 'Gumo', 'Gonsales', 'Migel']
    # ssert mexicans.count('Gumo') == 1
    result = 'Gumo' in mexicans
    assert result == True


# Parametrize (сумма параметров равна ожидаемому результату)

list = [1, 2, 3, 4]

@pytest.mark.parametrize('an_element_from_the_list', list)
def test_list_five(an_element_from_the_list):
    a = sum(list)
    assert a == 10


def test_set_one():
    numbers = [1, 2, 3, 2, 3, 4, 5]
    set_numbers = set(numbers)
    # print(set_numbers)
    set_numbers.add('666')
    # print(set_numbers)
    assert '666' in set_numbers
