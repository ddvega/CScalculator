def toBinary(number):

    if '.' not in str(number):
        return "{0:b}".format(number)

    else:
        whole, dec = str(number).split(".")
        whole = int(whole)
        dec = int(dec)
        res = bin(whole).lstrip("0b") + "."
        for x in range(11):
            whole, dec = str((decimal_converter(dec)) * 2).split(".")
            dec = int(dec)
            res += whole
    return res


def decimal_converter(num):
    while num > 1:
        num /= 10
    return num



print(toBinary(235.65))
print(toBinary(37))


