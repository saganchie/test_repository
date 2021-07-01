# while True:
#     recoding_st = input("Введите ваши символы \n")
#     if not recoding_st:
#         continue
#
#
#     def redecode_func(recoding_st):
#         res = ""
#         counter = 1
#         for el in range(len(recoding_st)):
#             if el(recoding_st) == el(recoding_st+1):
#                 counter += 1
#             else:

mystr = input()


def rle_encode(mystr):
    result = ""
    counter = 1
    for i in range(len(mystr) - 1):
        if mystr[i] == mystr[i + 1]:
            counter += 1
        else:
            if counter == 1:
                result += mystr[i]
            else:
                result += str(counter) + s[i]
            counter = 1
    if len(mystr) > 0:
        if counter > 1:
            result += str(counter) + mystr[-1]
        else:
            result += mystr[-1]
    return result


print(rle_encode(mystr))
