def int2words(integer):
    ones={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",
          8:"eight",9:"nine",10:"ten"}
    teens={11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",
           16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
    tens={20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",
          80:"eighty",90:"ninety"}
    while True:
        try:
            if 0<= integer <=10:
                word=ones[integer]
            elif 11<= integer <=19:
                word=teens[integer]
            elif 20<= integer <=99:
                if integer%10==0:
                    word=tens[integer]
                elif 0<= int(integer%10) <=9:
                    word=tens[integer-int(integer%10)]+"-"+ones[int(integer%10)]
            else:
                word="invalid"
            break
        except TypeError:
            return "invalid"
    return word

def dollars(floatx):
    temp=str(floatx)
    dollarsCents=temp.split(".")
    while True:
        try:
            word1= int2words(int(dollarsCents[0]))
            word2= int2words(int(dollarsCents[1]))
            break
        except ValueError:
            return "invalid"
   
    return word1,word2

###############

infile=open("dollar.txt")
outfile=open("dollarOUT.txt","w")
for line in infile:
    if "$" in line or "SGD" in line:
        if "$" in line:
            if dollars(line.strip("$"))!="invalid":
                print(line.strip("\n"),"is",dollars(line.strip("$"))[0],"dollars and",dollars(line.strip("$"))[1],"cents.",end=" ")
                print()
            else:
                print(line.strip("\n"),"is invalid.",end=" ")
                print()
        if "SGD" in line:
            if dollars(line.strip("SGD"))!="invalid":
                print(line.strip("\n"),"is",dollars(line.strip("SGD"))[0],"dollars and",dollars(line.strip("SGD"))[1],"cents.",end=" ")
                print()
            else:
                print(line.strip("\n"),"is invalid.",end=" ")
                print()        
    else:
        print(line.strip("\n"),"is invalid.",end=" ")
        print()
'''printing the above on the shell'''

infile=open("dollar.txt") 
for line in infile:
    if "$" in line or "SGD" in line:
        if "$" in line:
            if dollars(line.strip("$"))!="invalid":
                print(line.strip("\n"),"is",dollars(line.strip("$"))[0],"dollars and",dollars(line.strip("$"))[1],"cents.",file=outfile)
                print()
            else:
                print(line.strip("\n"),"is invalid.",file=outfile)
                print()
        if "SGD" in line:
            if dollars(line.strip("SGD"))!="invalid":
                print(line.strip("\n"),"is",dollars(line.strip("SGD"))[0],"dollars and",dollars(line.strip("SGD"))[1],"cents.",file=outfile)
                print()
            else:
                print(line.strip("\n"),"is invalid.",file=outfile)
                print()        
    else:
        print(line.strip("\n"),"is invalid.",file=outfile)
        print()

    
outfile.close()   
   
    
