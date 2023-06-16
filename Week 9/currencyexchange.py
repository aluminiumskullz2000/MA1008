SGD = input("To or from Singapore dollar (T/F): ")
number = 0
modes = "To"
if SGD == "T":
    number = float(input("Amount in Ringgit Malaysia: "))
elif SGD == "F":
    number = float(input("Amount in Singapore Dollar: "))
    modes = "From"

def exchangeAmount(amount, mode):
    if mode == "To":
        currency = amount / 3.05
        print("RM{:.2f} = S${:.2f}".format(amount,currency))
    elif mode == "From":
        currency = amount * 3.05
        print("S${:.2f} = RM{:.2f}".format(amount,currency))

exchangeAmount(number,modes)
