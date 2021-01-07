This is a Hamming ECC program. It is a command line program that will take a .txt file as an argument. 

$ python test.py <filename>

This will add the Hamming bits to each byte of information in the text file, creating a file "transfer.txt" in the "data" folder. 
It will then pass this file through a corruption program simulating the flipping of bits that could happen during some data transfers. 
This creates a "corruptTransfer.txt" file in the "data" folder. 
The program will then run this file through the ECC correction program fixing the mistakes and creating a "fixed.txt" file. 
It will also send the "corruptTransfer.txt" file to a program that will just remove the extra ECC bits creating a "corrupt.txt" file for comparison with "fixed.txt". This will give better visual representation of how the file would have been junk had it not had the Hamming ECC bits added and used to correct the corrupted file. 

Thank you for using my program!