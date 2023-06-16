
""" Adapted from http://www.prasannatech.net/2012/07/eight-queens-python.html
    Author: S.Prasanna

    There are many other solutions to this problem available online. This one 
    is quite easy to understand.
    Make sure to credit other peoples code when used - and it is not acceptable to use 
    other peoples code as the entire solution for your assignments!!!
"""
board = []
size = 8

#A function which checks if a particular row and col is dangerous (i.e.,
#queen could be taken if placed there)
def danger(row, col):
    """ Return if there is a danger by placing queen in
        a given row, col
    """
    for (i, j) in board:
        if row == i: return True
        if col == j: return True
        if abs(row - i) == abs(col - j): return True
    return False

#A function which calculates the whole solution    
def placequeen(row):
    #If row is bigger than size, we've finished - so print answer
    if row > size:
        print(board)
    #If size <= row we still have more to place        
    else:
        #try placing queen
        for col in range(1, size + 1):
            #is it safe?
            if not danger(row, col):
                board.append((row, col))
                placequeen(row + 1)
                board.remove((row,col))

#Run the main method, starts by plaing the first queen
placequeen(1)
