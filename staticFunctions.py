import texteditor

# write data to .txt file '''
def write(data):
    # create output file
    out_file = open("calc_history.txt", "w")

    # add elements in self.history to .txt file
    for i in range(len(data)):
        out_file.write(data[i] + '.\n')
    out_file.close()


# calculator class
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