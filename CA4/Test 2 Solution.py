# Program to read a report in file and count words with different number of vowels
# Algorithm:
#    Use a dictionary to store counts of words with different number of vowels,
#    with the number of vowels as the key and the count as the value
#    Open input file and read it line by line
#    For each line
#       Split it into words which are separated by " "
#       For each word
#          Count the number of vowels in the word
#          Add each count appropriately to the dictionary
#
#    Print the results to output file

def CountVowel(word):  # function to count the number of vowels in a word 

    vowels = 0
    for c in word:  # take each character in the word
        if c in "aeiouAEIOU":   # see if it is in the string of vowels
            vowels += 1
    return vowels

while True:  # open the file
    filename = input("Enter the filename: ")
    try:
       infile = open(filename, "r")
       break
    except FileNotFoundError:
       print("File not found. Try again.")

while True:
    filename = input("Enter output filename: ")
    try:
       outfile = open(filename, "w")
       break
    except OSError:
       print("File not found. Try again.")

vowelCount = {}  # create a dictionary to store the vowel count
maxVowels = 0

for L in infile:  # for each line in the file
    wordList = L.split()  # split L into words using " "
    for word in wordList:   # take each word
        vowels = CountVowel(word)   # count the vowels
        if vowels > maxVowels:# remember the maximum count
            maxVowels = vowels
        if vowels in vowelCount:  # add 1 to a particular count
            vowelCount[vowels] += 1
        else:
            vowelCount[vowels] = 1  # create dictionary item if not already in

print("Number of vowels      Word Count", file=outfile)
print("================      ==========", file=outfile)
for i in range(0, maxVowels+1):
    if (i in vowelCount):
       print("      {:2d}                 {:3d}".format(i, vowelCount[i]), file=outfile)

infile.close()
outfile.close()
