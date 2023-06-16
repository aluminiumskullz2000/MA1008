x = [[1,2,3],[4,5,6],[7,8,9]]
print("Matrix:")
for a in x:
    for b in a:
        print((f'{b:^3d}'), end="")
    print () 
print ('\nTranspose Matrix: ')
for a in x:
    print ((f'{a[0]:^3d}'), end= "")
print()
for a in x:
    print ((f'{a[1]:^3d}'), end= "")
print()
for a in x:
    print ((f'{a[2]:^3d}'), end= "")