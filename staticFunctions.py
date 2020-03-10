import texteditor


def decToBinary(bsize, num):
    binary = ''

    sizes = ['8', '12', '16', '20', '24', '32']

    maxNum = [255, 4095, 65535, 1048575, 16777215, 4294967295]

    for i in range(len(sizes)):
        if bsize == sizes[i]:
            if num <= maxNum[i]:
                temp = '{:00' + sizes[i] + 'b}'
                return str(temp.format(num))
            else:
                return "{} doesn't fit in {} bits".format(str(num), sizes[i])

    return str(binary)
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


# calculator class
