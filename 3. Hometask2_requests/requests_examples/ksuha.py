# def test_commentary(color):
#     if color == 'red':
#         return "It's a tomato."
#     elif color == "green":
#         return "It's a green pepper."
#     elif color == 'bee purple':
#         return "I don't know what it is, but only bees can see it."
#     else:
#         return "I've never heard of the color " + color + "."
#
#
# print(test_commentary('rwowo'))
# # print(comment)


# def menu(wine, entree, dessert='montenegro'):
#     print({'wine': wine, 'entree': entree, 'dessert': dessert})
#
#
# menu('chardonnay', 'chicken', 'werwerwer')

# def outer(a, b):
#     def inner(c, d):
#         return c + d
#
#     return inner(a, b)
#
# print(outer(1,4))

# def knights(saying):
#     def inner(quote):
#         return "We are the knights who say: '%s'" % quote
#
#     return inner(saying)
#
# print(knights('Hello!'))

# def knights2(saying):
#     def inner2():
#         return "We are the knights who say: '%s'" % saying
#
#     # return inner2
#
# print(knights2('Privet!'))

# def edit_story(words, func):
#     for word in words:
#         print(func(word))
#
#
# stairs = ['thud', 'meow', 'thud', 'hiss']
#
#
# def enliven(word):  # больше эмоций!
#     return word.capitalize() + '!'
#
#
# edit_story(stairs, enliven)

# def my_range(first=0, last=10, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
#
# ranger = my_range()
#
# for x in ranger:
#     print(x)

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result

    return new_function


# def add_ints(a, b):
#     return a + b
#
#
# # print(add_ints(3, 5))
#
# cooler_add_ints = document_it(add_ints)
# print(cooler_add_ints(7, 8))

@document_it
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))
