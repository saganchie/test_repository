# while True:
#     underscore_symbols = input("Введите ваши символы \n")
#     if not underscore_symbols:
#         continue
#     print(underscore_symbols, r'\d{0,4}[A-Za-z]{1}')

while True:
    coding_st = input("Введите ваши символы \n")
    if not coding_st:
        continue


    def decode_func(coding_st):
        repeat = ""
        res = ""
        for e in coding_st:
            if e.isdigit():
                repeat += e
            else:
                if repeat:
                    res += e * int(repeat)
                else:
                    res += e
                repeat = ""
        return res


    print(decode_func(coding_st))
