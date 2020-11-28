import hamming
import corrupt
import process
import sys


if len(sys.argv) >= 2:
    filename = sys.argv[1]
    process.encode(filename, "data/transfer.txt")
    corrupt.simulateTransfer("data/transfer.txt", "data/corruptTransfer.txt")
    process.decode("data/corruptTransfer.txt", "corrupt.txt")
    process.decodeFix("data/corruptTransfer.txt", "fixed.txt")

else:
    print("Usage: $ test.py <filename> ")
    print("\t To test the Hamming ECC program, on <filename>")
    print("""\t Program will create two data files in data/ and two files in working directory
    \t data/
     \t\t transfer.txt - <filename> with added Hamming ECC. Ready for transfer
     \t\t corruptTransfer.txt - transfer.txt after one bit per byte is flipped
     \t corrupt.txt - the corrupt version of <filename> without Hamming ECC
     \t fixed.txt - corruptTransfer.txt fixed using Hamming ECC.""")