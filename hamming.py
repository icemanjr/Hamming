# Hamming code uses formula 2 ^ r >= m + r + 1
# r = number of redundant bits
# m = length of binary number


def addHam(value):
    if isBinary(value):
        m = len(value)
        r = calcRedundBits(m)
        data = redundBitPos(value, r)
        data = calcParity(data, r)

        return data
    else:
        print("Error: addHam() takes a binary input")


def checkHam(value):
    if isBinary(value):
        m = len(value)
        r = calcRedundBits(m)
        error = findError(value, r)
        if error != 0:
            print(error)
            if value[error] == '1':
                value = value[:-error] + '0' + value[-(error - 1):]
            else:
                value = value[:-error] + '1' + value[-error:]
        for i in range(r, 1, -1):
            value = value[:-(2**i)] + value[-(2**i - 1):]
        if r >= 2:
            value = value[:-2]
        return value

    else:
        print("Error: checkHam takes a binary input")


def findError(arr, nr):
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
    for i in str(val):
        if i in '10':
            binary = True
        else:
            binary = False
            break
        return binary


def calcRedundBits(m):
    for r in range(m):
        if 2**r >= m + r + 1:
            return r


def redundBitPos(data, r):
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


def calcParity(arr, r):
    n = len(arr)

    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            print(j, i)
            temp = j & (2 ** i) == (2 ** i)
            if temp:
                print(str(temp) + " : " + arr[-j])
                val = val ^ int(arr[-j])
        print(val)
        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr

