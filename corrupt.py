import random


# code to flip a single bit in a bitstring.

def simulateTransfer(filename, newFile):
    # Simulates the transfer of a file over a bad connection. Specifically it will corrupt a single bit per byte.
    file = open(filename, "r")
    cFile = open(newFile, "w")
    line = file.readline()
    line = line.split(" ")
    for c in line:
        if c != "":
            num = corrupt(c)
            cFile.write(num + " ")

    file.close()
    cFile.close()


def corrupt(data):
    # Flip a single bit in the given string of 1's and 0's
    data_list = list(data)
    rand = random.randint(1, len(data))
    data_list[-rand] = str(int(data_list[-rand]) ^ 1)

    data = ''.join(map(str, data_list))

    return data
