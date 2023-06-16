Birthday = {"S1234567F": (10/12/2020)}
def insert(ICnumber, birthdate, Birthday = Birthday):
    if ICnumber not in Birthday:
        Birthday[ICnumber] = birthdate

def check_birthday(ICnumber, birthdate, Birthday = Birthday):
    if ICnumber in Birthday:
        if Birthday[ICnumber] == birthdate:
            return 1
        else:
            return 3
    else:
        return 2
