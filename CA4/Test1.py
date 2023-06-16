def wordlength(word):  # function to count word length without punctuation 
    if (word[-1] in ".,;!?:\n"):  # check if last character a punctuation
        return len(word)-1
    return len(word)

while True:
    k = input("Enter input filename: ")
    try:
        infile = open(k,"r")
        break
    except FileNotFoundError:
        print("Please edit the name of file.")
        
while True:
    j = input("Enter output filename: ")
    try:
        outfile = open(j, "w")
        break
    except FileNotFoundError:
        print("Please edit the name of file.")



lengths = {}
maxlength = 0

for L in infile:
    wordlist = L.split()
    for word in wordlist:
        length = wordlength(word)
        if length > maxlength:
            maxlength = length
        if length in lengths:
            lengths[length] += 1
        else:
            lengths[length] = 1

print("Word Length     Word Count", file = outfile)
print("   ===             ===    ", file = outfile)

for i in range(1, maxlength + 1):
    if (i in lengths):
        print("    {:2d}         {:3d}".format(i ,lengths[i]),file = outfile)
      
infile.close()
outfile.close()
              
