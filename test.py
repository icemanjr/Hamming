import hamming

input = "11111111"
desired_output = "101011101110"
wError = "101001111011"

output = hamming.addHam(input)
print("input: " + input)
print("Actual: " + output)

output = "111101100111"

eOutput = hamming.checkHam(output)
r = hamming.calcRedundBits(len(output))
error = hamming.findError(output, r)
print("Error found in bit: " + str(error))
print("Error in bit corrected?: \nActual: " + eOutput)

