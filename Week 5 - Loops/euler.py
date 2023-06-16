# e = 1
# x = 1

# for i in range (1,100):
#     x = x*i
#     e += (1/x)

# print (e)

epsilon = 1e-8
e = 0
growing_term = 1/1
deno = 1
multiplier = 1

while growing_term > epsilon:
    e += growing_term
    deno = deno * multiplier
    multiplier += 1
    growing_term = 1/deno
print (e)