def mile_in_m(miles):
    miles_meters = miles * 1609
    return miles_meters


while True:
    value = input("Введите ваши параметры \n")
    if not value:
        continue
    split_result = value.split(" ")
    miles_conv = mile_in_m(float(split_result[0]))
    print(miles_conv)