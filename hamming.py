# Hamming code uses formula 2 ^ r >= m + r + 1
# r = number of redundant bits
# m = length of binary number


def addHam(value):
    # Adds a Hamming ECC to a given string of 1's and 0's
    if isBinary(value):
        m = len(value)
        r = calcRedundBits(m)
        data = redundBitPos(value, r)
        data = calcParity(data)

        return data
    else:
        print("Error: addHam() takes a binary input")


def checkHam(value):
    # Checks the given string that has been encoded with Hamming ECC for errors and corrects them.
    if isBinary(value):
        m = len(value)
        r = calcRedundBits(m)
        error = findError(value, r)
        if error != 0:
            value_list = list(value)
            if value_list[-error] == '1':
                value_list[-error] = '0'
            else:
                value_list[-error] = '1'
            value = ''.join(map(str, value_list))
        return value

    else:
        print("Error: checkHam takes a binary input")


def removeHam(value):
    # Removes parity bits from string that has Hamming ECC
    if isBinary(value):
        m = len(value)
        r = calcRedundBitsHammed(m)
        value_list = list(value)
        for i in range(r):
            value_list.pop(m - (2**i))
        result = ''.join(map(str, value_list))
        return result


def findError(arr, nr):
    # Checks string with Hamming ECC for errors
    n = len(arr)
    result = 0

    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(arr[-1 * j])

        result = result + val * (10**i)
    return int(str(result), 2)


def isBinary(val):
    # Evaluates if a given string contains only 1's and 0's
    binary = True
    for i in str(val):
        if i not in '10':
            binary = False
            break
    return binary


def calcRedundBits(m):
    # Calculates the number of parity bits required to add Hamming ECC to binary number with m digits
    for r in range(m):
        if 2**r >= m + r + 1:
            return r

def calcRedundBitsHammed(m):
    # Calculates how many parity bits there would be in a Hamming ECC encoded binary number with m digits
    for r in range(m):
        if 2**r >= m:
            return r


def redundBitPos(data, r):
    # Calculates the position of parity bits, and inserts 0's in their positions
    j = 0
    k = 1
    m = len(data)
    result = ''

    for i in range(1, m + r + 1):
        if i == 2**j:
            result = result + '0'
            j += 1
        else:
            result = result + data[-k]
            k += 1

    return result[::-1]


def calcParity(data):
    # Given binary number with extra parity bits added as 0's, Calculates the value for each of those parity bits.
    ch = 0
    data = list(data)
    data.reverse()

    for parity in range(0, len(data)):
        ph = (2**ch)
        if ph == (parity + 1):
            startIndex = ph - 1
            i = startIndex
            toXor = []

            while i < len(data):
                block = data[i:i + ph]
                toXor.extend(block)
                i += 2*ph

            for z in range(1, len(toXor)):
                data[startIndex] = int(data[startIndex])^int(toXor[z])
            ch += 1

    data.reverse()
    data = ''.join(map(str, data))
    return data
