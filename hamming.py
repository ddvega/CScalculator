import math
from numpy import asarray


# make space by adding empty bits to hamming code in the correct positions
def addBits(e, b, bnum):
    bList = list(bnum)
    new = []
    errorBits = [0, 1, 3, 7, 15, 31]
    for i in range(b + e):
        if i in errorBits:
            new.append(7)
        else:
            new.append(bList.pop(0))
    return new


# convert number to hamming code
def encode(ext, b, blist, oddEven):
    # elements of interest per row
    second = [1, 2, 5, 6, 9, 10, 13, 14, 17, 18, 21, 22, 25, 26, 29, 30, 33,
              34, 37]
    third = [3, 4, 5, 6, 11, 12, 13, 14, 19, 20, 21, 22, 27, 28, 29, 30, 35,
             36, 37]
    fourth = [7, 8, 9, 10, 11, 12, 13, 14, 23, 24, 25, 26, 27, 28, 29, 30]
    fifth = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    sixth = [31, 32, 33, 34, 35, 36, 37]

    # build matrix
    m = [[0 for y in range(b + ext)] for x in range(ext)]

    # populate matrix
    for i in range(ext):
        for j in range(b + ext):

            # first row every other element
            if i == 0:
                if j % 2 == 0:
                    m[i][j] = int(blist[j])
                else:
                    m[i][j] = 9

            # second row every two elements
            if i == 1:
                if j in second:
                    m[i][j] = int(blist[j])
                else:
                    m[i][j] = 9

            # third row every 4 elements
            if i == 2:
                if j in third:
                    m[i][j] = int(blist[j])
                else:
                    m[i][j] = 9

            # fourth row every 8 elements
            if i == 3:
                if j in fourth:
                    m[i][j] = int(blist[j])
                else:
                    m[i][j] = 9

            # fifth row every 16 elements
            if i == 4:
                if j in fifth:
                    m[i][j] = int(blist[j])
                else:
                    m[i][j] = 9

            # 6th row every 32 elements
            if i == 5:
                if j in sixth:
                    m[i][j] = int(blist[j])
                else:
                    m[i][j] = 9

    # fill error bits
    for i in range(ext):
        cnt1 = m[i].count(1)
        
        #track ...
        tracker = 0
        for j in range(b + ext):
            
            if oddEven == 'even' and cnt1 % 2 == 0 and m[i][j] == 7:
                m[i][j] = 0

            elif oddEven == 'even' and not cnt1 % 2 == 0 and m[i][j] == 7:
                
                if tracker == 0:
                    m[i][j] = 1
                    tracker += 1

                else:
                    m[i][j] = 0
                
            elif oddEven == 'odd' and not cnt1 % 2 == 0 and m[i][j] == 7:
                m[i][j] = 0
                
            elif oddEven == 'odd' and cnt1 % 2 == 0 and m[i][j] == 7:
                
                if tracker == 0:
                    m[i][j] = 1
                    tracker += 1
                    
                else:
                    m[i][j] = 0

    # loop through columns to get hamming code
    npa = asarray(m)
    hammingCode = ""

    for column in npa.T:
        if 0 in column:
            hammingCode += '0'
        if 1 in column:
            hammingCode += '1'

    return hammingCode


def hamCodeGenerator(bitNum, number, evenOdd):
    binary = None

    # make sure hamming code fits
    if bitNum == 8 and number > 251:
        return "need 16bits"

    if bitNum == 16 and number > 65530:
        return "need 32bits"

    # convert dec to binary
    if bitNum == 8:
        binary = '{:008b}'.format(number)
    elif bitNum == 16:
        binary = '{:016b}'.format(number)
    elif bitNum == 32:
        binary = '{:032b}'.format(number)

    # add binBits to binary code
    binBits = len(binary)
    errBits = math.floor(math.log2(binBits) + 1)
    ham = addBits(errBits, binBits, binary)

    return encode(errBits, binBits, ham, evenOdd)


def hamCodeRead(hcode):
    # convert code to list
    hList = list(hcode)

    # locations of error bits
    errorBits = [0, 1, 3, 7, 15, 31]

    # binary value string
    s = ""

    # add values to string
    for i in range(len(hList)):
        if i not in errorBits:
            s += hList[i]

    return str(int(s, base=2))
