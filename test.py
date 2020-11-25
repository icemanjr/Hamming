import hamming
import corrupt
import process
import sys


filename = sys.argv[1]
process.transfer(filename, "transfer.txt")
process.decode("transfer.txt", "decoded.txt")

# input = "010010101"
#
# output = hamming.addHam(input)
# print("input: " + input)
# print("Actual: " + output)
#
# eOutput = corrupt.corrupt(output)
# print("Output after corruption of a single bit: " + eOutput)
#
# cOutput = hamming.checkHam(eOutput)
# r = hamming.calcRedundBits(len(eOutput))
# error = hamming.findError(eOutput, r)
# print("Error found in bit: " + str(error))
# print("Error corrected? " + cOutput)

