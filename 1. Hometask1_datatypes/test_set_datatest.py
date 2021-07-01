from typing import Set
import pytest

# Объединяем два множества, проверка длины

def test_set_zero():
    week = {'Monday','Tuesday','Wednesday', 'Thursday', 'Friday'}
    weekend = {'Saturday', 'Sunday'}
    all_week = week | weekend
    len_week = len(all_week)
    assert len_week == 7

# Создаем множество из списка при помощи set.
# Проверяем, что во множество был добавлен элемент
# и он есть в этом множестве

def test_set_one():
    numbers = [1, 2, 3, 2, 3, 4, 5]
    set_numbers = set(numbers)
    # print(set_numbers)
    set_numbers.add('666')
    # print(set_numbers)
    assert '666' in set_numbers


"""

Создаем множество из списка при помощи set.
Проверяем, что из множества был удален элемент
и его нет в этом множестве

"""


def test_set_two():
    days = ['Monday', 'Tuesday', 'Saturday', 'Friday', 'Monday']
    set_days = set(days)
    # print(set_days)"
    set_days.remove('Friday')
    # print(set_days)
    assert 'Friday' not in set_days


# Объединяем множества, проверяем, что подмножество входит во множество

def test_set_three():
    set_one = {'Patrick', 'Ksuha'}
    set_two = {'Serega', 'Jeka'}
    all_set = set_one.union(set_two)
    # print(all_set)
    assert set_one.issubset(all_set)


# Параметризация

set1 = [{'Patrick', 'Ksuha', 'Serega', 'Elchugin'}, {'Elchugin', 'Rita', 'Grishina'}]
set2 = [{'Elchugin', 'Rita', 'Grishina'}, {'Rita', 'Grishina'}]


@pytest.mark.parametrize('an_element_in_the_set', (set1, set2))
def test_set_four(an_element_in_the_set):
    new_set = an_element_in_the_set[0] ^ an_element_in_the_set[1]
    print(new_set)
    assert 'Elchugin' not in new_set
