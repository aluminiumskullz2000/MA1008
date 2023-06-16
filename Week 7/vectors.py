vector1 = input("Please input first vector x,y,z: ")
vector2 = input("Please input second vector x,y,z: ")
vec1 = vector1.split(",")
vec2 = vector2.split(",")
for x in range(len(vec1)):
    vec1[x] = int(vec1[x])
for y in range(len(vec2)):
    vec2[y] = int(vec2[y])

sum = (vec1[0] + vec2[0]), (vec1[1] + vec2[1]) , (vec1[2] + vec2[2])
print ("sum of vectors = ", sum)

dotproduct =  vec1[0]*vec2[0] + vec1[1]*vec2[1] + vec1[2]*vec2[2]
print ("dot product = ", dotproduct)