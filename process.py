# To bring a file and add a Hamming ECC to be ready for transfer.
# Then to corrupt a single bit per line, to simulate data corruption during transfer.
# Then to make a copy without the ECC to show the corrupt file.
# Then to fix the file using the Hamming ECC. Ending with 4 different files.
# 1st the file_transfer.txt, 2nd the transfer_corrupt.txt, 3rd the corrupt.txt, and 4th the file_fixed.txt
import hamming


def encode(filename, newFile):
    # Add a Hamming ECC to <filename> and save it to <newFile>
    file = open(filename, "rb")
    trans = open(newFile, "w")

    for line in file:
        for j in range(len(line)):
            bin = "{0:b}".format(line[j])
            nline = hamming.addHam(bin)
            trans.write(nline + " ")

    file.close()
    trans.close()


def decode(filename, newFile):
    # Remove the Hamming ECC parity bits from <filename> and save it as <newFile>
    # Note: This does not check the Hamming ECC for errors before removing parity bits
    file = open(filename, "r")
    decode = open(newFile, "w")

    for line in file:
        line = line.split(" ")
        for c in line:
            if c != "":
                nline = hamming.removeHam(c)
                num = int(nline, 2)
                ch = chr(num)
                decode.write(ch)

    file.close()
    decode.close()


def decodeFix(filename, newFile):
    # Check the Hamming ECC for errors in <filename>, correct those errors and save the file to <newFile>
    file = open(filename, "r")
    decode = open(newFile, "w")

    for line in file:
        line = line.split(" ")
        for c in line:
            if c != "":
                nline = hamming.checkHam(c)
                nline = hamming.removeHam(nline)
                num = int(nline, 2)
                ch = chr(num)
                decode.write(ch)

    file.close()
    decode.close()