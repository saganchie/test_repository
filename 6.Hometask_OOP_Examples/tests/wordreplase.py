
while True:
    underscore_symbols = (input("Введите ваши символы \n").replace("_", " ").title().replace(" ", ""))
    if not underscore_symbols:
        continue
    print(underscore_symbols)
