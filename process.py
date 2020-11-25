# To bring a file and add a Hamming ECC to be ready for transfer.
# Then to corrupt a single bit per line, to simulate data corruption during transfer.
# Then to make a copy without the ECC to show the corrupt file.
# Then to fix the file using the Hamming ECC. Ending with 4 different files.
# 1st the file_transfer.txt, 2nd the transfer_corrupt.txt, 3rd the corrupt.txt, and 4th the file_fixed.txt
import hamming


def transfer(filename, newFile):
    file = open(filename, "rb")
    trans = open(newFile, "w")

    line = file.readline()
    for j in range(len(line)):
        bin = "{0:b}".format(line[j])
        nline = hamming.addHam(bin)
        trans.write(nline + " ")

    file.close()
    trans.close()


def decode(filename, newFile):
    file = open(filename, "r")
    decode = open(newFile, "w")

    line = file.readline()
    line = line.split(" ")
    for c in line:
        if c != "":
            nline = hamming.removeHam(c)
            print(nline)
            print("Should be: " + str(ord('H')))
            num = int(nline, 2)
            num = int(num)
            print(num)
            ch = chr(num)
            print(ch)
            decode.write(ch)

    file.close()
    decode.close()
