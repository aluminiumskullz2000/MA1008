# CA 2 Program C v2
# Students and marks for maths, physics and chemistry

student  = 0  # initialise the variables
m_total = 0
p_total = 0
c_total = 0
cont = True  # variable for continuing

while cont:  # loop to go round asking for marks of students
   student += 1
   print("Student", student)
   while True: 
      m = int(input("   Maths marks (0-100): "))
      if m >= 0 and m <= 100:
         break
   while True: 
      p = int(input("   Physics marks (0-100): "))
      if p >= 0 and p <= 100:
         break
   while True: 
      c = int(input("   Chemistry marks (0-100): "))
      if c >= 0 and c <= 100:
         break

   ave = (m + p + c) / 3   # find the average
   if (ave >= 80):
      grade = "A"
   elif (ave >= 70):
      grade = "B"
   elif (ave >= 60):
      grade = "C"
   elif (ave >= 50):
      grade = "D"
   else:
      grade = "F"

   print("Average marks of Student {:2d} = {:0.2f}, Grade is {:1s}".\
         format(student, ave, grade))
   m_total += m
   p_total += p
   c_total += c

   yes = input("Any more students? (Y or N): ")
   cont = yes == "Y" or yes == "y"  # determine if to continue

# After input, find overall results
m_ave = m_total/student
p_ave = p_total/student
c_ave = c_total/student
print("Class average: Maths {:0.2f}, Physics {:0.2f}, Chemistry {:0.2f}".\
      format(m_ave, p_ave, c_ave))
print("The overall average: {:0.2f}". format((m_ave+p_ave+c_ave)/3))
   
