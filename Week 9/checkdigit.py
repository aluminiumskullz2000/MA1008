numbers = ["1","2","3","4","5","6","7","8","9","0"]
def check_digit(string, integer = -1):
    character = string[integer]
    if integer > len(string):
        return False
    elif character in numbers:
        return True
    else:
        return False