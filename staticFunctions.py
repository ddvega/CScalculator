import texteditor
from numpy import binary_repr


def decToBinary(num, size):
    return str(binary_repr(int(num), width=int(size)))


def floatToBinary(num, places):
    places = int(places)
    whole, dec = num.split(".")
    whole = int(whole)
    dec = int(dec)
    res = str(binary_repr(whole, width=places)) + '.'

    for x in range(places):
        whole, dec = str((decimal_converter(dec)) * 2).split(".")
        dec = int(dec)
        res += whole

    return str(res)


def decimal_converter(num):
    while num > 1:
        num /= 10
    return num


def binaryToDec(snum, type):
    if type == 'signed':
        x = int(snum, 2)
        if snum[0] == '1':  # "sign bit", big-endian
            x -= 2 ** len(snum)
        return str(x)
    else:
        return str(int(snum, 2))


def fixZeros(s):
    s = list(s)
    i = 0
    while True:
        if i == 0:
            if s[i] == '0' and s[i + 1].isdigit():
                s.pop(i)
                i -= 1
        elif i == len(s) - 1 or len(s) < 3:
            break
        elif s[i] == '0' and not s[i - 1].isdigit() and s[i + 1].isdigit():
            s.pop(i)
            i -= 1
        i += 1

    return "".join(s)


def show_read_me():
    texteditor.open(filename='manual.txt')


# write data to .txt file '''
def write(data):
    # create output file
    out_file = open("calc_history.txt", "w")

    # add elements in self.history to .txt file
    for i in range(len(data)):
        out_file.write(data[i] + '.\n')
    out_file.close()


def to_int(bin):
    x = int(bin, 2)
    if bin[0] == '1':  # "sign bit", big-endian
        x -= 2 ** len(bin)
    return x
