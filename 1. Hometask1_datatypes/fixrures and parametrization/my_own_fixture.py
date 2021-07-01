import pytest

# моя  фикстура
@pytest.fixture
def my_first_fixture():
    print("===>\n Print from 'my_first_fixture'")

    """
    Пробую запилить фикстуру
    
    """
@pytest.fixture()
def my_second_fixture():
    """
    Возвращаем none
    """
    print("===>\n Print from 'second fixture'")
    return None

def test_one(my_first_fixture):
    print("Vse budet horosho")
    pass

def test_two(my_second_fixture):
    print("Vse budet horosho2")
    pass

class TestFunctoion:

    def test_from_test_class_one(self, my_first_fixture):
        pass
    def test_from_test_class_two(self, my_first_fixture, my_second_fixture):
        pass