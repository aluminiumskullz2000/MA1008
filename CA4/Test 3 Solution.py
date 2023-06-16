# Program to read in weights and generate counts for three categories
# Erroneous data are picked out and not counted
# The algorithm converts individual lines in the input file to numbers and check
# for the category.
#
# Algorithm:
# Open the file
# Read the file line by line
# Split the line into strings based on ","
# For each component string
#    Convert it to float
#    If conversion fails, it's erroneous input
#    Else place it in its category and increase the category count by 1
#
# Print the results

def category(weight):   # function to determine the category based on weight
   if weight >= 85:
       return "over"
   elif weight >= 55:
       return "good"
   else:
       return "under"
    

while True:
   filename = input("Enter input filename: ")
   try:
      infile = open(filename, "r")
      break
   except FileNotFoundError:
      print("No such file. Enter filename again.")

while True:
   filename = input("Enter output filename: ")
   try:
      outfile = open(filename, "w")
      break
   except OSError:
      print("No such file. Enter filename again.")
      
over = 0   # initialise the counters
good = 0
under = 0
error = 0

for L in infile:          # L takes each line of text in the file
    items = L.split(",")  # Split L by "," into a list of items

    for item in items:    # Take each item
       try:               # Try to catch error
          num = float(item)    # convert it into a floating point number
          cat = category(num)  # determine the category
          if cat == "over":
             over += 1
          elif cat == "good":
             good += 1
          else:  # must be "under" here
             under += 1
       except ValueError:  # error occurred because item is not a number
          error += 1

print("Overwight people:   ", over, file=outfile)
print("Good-weight people: ", good, file=outfile)
print("Underweight people: ", under, file=outfile)
print("Number of errors:   ", error, file=outfile)

infile.close()
outfile.close()
