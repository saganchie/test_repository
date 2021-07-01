furry = False
small = False


def test_testovik():
    if furry:
        if small:
            print("It's a cat.")
        else:
            print("It's a bear!")
    else:
        if small:
            print("It's a skink!")
        else:
            print("It's a human. Or a hairless bear.")


color = "bee purple"


def test_color():
    if color == "red":
        print("It's a tomato")
    elif color == "green":
        print("It's a green pepper")
    elif color == "bee purple":
        print("I don't know what it is, but only bees can see it")
    else:
        print("I've never heard of the color", color)


def test_count():
    count = 1
    while count <= 5:
        print(count)
    count += 1


def test_test_while():
    numbers = [1, 3, 5]
    position = 0
    while position < len(numbers):
        number = numbers[position]
        if number % 2 == 0:
            print('Found even number', number)
            break
        position += 1
    else:  # break not called
        print('No even number found')


def test_rabbit():
    rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
    for rabbit in rabbits:
        print(rabbit[0:5])
    # current = 0
    # while current < len(rabbits):
    #     print(rabbits[current])
    #     current += 1


def test_cheeses():
    cheeses = []
    for cheese in cheeses:
        print('This shop has some lovely', cheese)
        break
    else:  # отсутствие прерывания означает, что сыра нет
        print('This is not much of a cheese shop, is it?')


def test_interprise():
    days = ['Monday', 'Tuesday', 'Wednesday']
    fruits = ['banana', 'orange', 'peach']
    drinks = ['coffee', 'tea', 'beer']
    desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
    for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
        print(day, ": - drink", drink, " - eat", fruit, " - enjoy", dessert)


def test_new_tuple():
    english = 'Monday', 'Tuesday', 'Wednesday'
    french = 'Lundi', 'Mardi', 'Mercredi'
    print(zip(english, french))


def test_number_list():
    number_list = []
    for dict_elements in range(1, 6):
        number_list.append(dict_elements)
    print(number_list)


def test_agree():
    return True


def agree():
    return False


def test_return():
    if agree():
        print('Spleniddid!')
    else:
        print('Nononono')


def test_echo(anything):
    return anything + ' ' + anything


print(test_echo('dasdasd'))
