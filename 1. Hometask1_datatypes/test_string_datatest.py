import pytest


# тесты с типом данных string

def test_string_one():
    second_name = 'Evgeniy'
    assert second_name[0] == 'E'


def test_string_two():
    long_name = 'evgeniysaganchy'
    assert long_name[7:] == 'saganchy'


def test_string_three():
    big_name = 'saganchi_evgeniy' + '_igorevich'
    assert big_name == 'saganchi_evgeniy_igorevich'


@pytest.mark.parametrize("test_input", [(3, 3), (6, 6), (7, 7)])
def test_string_four(test_input):
    assert test_input[0] - test_input[1] == 0


# Parametrize

def test_string_five():
    hight_string = 'shkola'
    assert hight_string.capitalize() == 'Shkola'
