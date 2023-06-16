# You have a class of students, each taking two subjects, maths and physics. Write a program that
# reads in the marks for the two subjects for each student. Your program should reject any marks
# outside the range 0 – 100, inclusive, and require the user to provide it again. After reading in the
# marks of each student, print his/her average marks and the grade. The grade is awarded according to
# these scores:
#  80 <= A <= 100, 70 <= B < 80, 60 <= C < 70, 50 <= D < 60, F < 50.
# Then your program should enquire if there’s any more input. Continue if yes, and exit input if no.
# Upon exiting the inputs, print the class average for each subject. Here is a sample dialogue.
# Underlined texts are inputs.
# Student 1
#  Enter maths score: 55
#  Enter physics score: 72
#  Average: 63.50, Grade: C
# Any more students? Y
# Student 2
#  Enter maths score: 80
#  Enter physics score: 93
#  Average: 86.50, Grade: A
# Any more students? N
# Class average: Maths 67.50, Physics 82.50
# The example shows only two students. Your program should handle as many as there are students.

cont = True
students = 0
math_score = 0
physics_score = 0

while cont:
    students +=1
    print("Student", students)
    while True: 
      m = int(input("   Maths marks (0-100): "))
      if m >= 0 and m <= 100:
         break
    while True: 
      p = int(input("   Physics marks (0-100): "))
      if p >= 0 and p <= 100:
         break
    ave = (math_score + physics_score) /2
    if ave >= 80:
        grade = "A"
    elif (ave >= 70):
      grade = "B"
    elif (ave >= 60):
      grade = "C"
    elif (ave >= 50):
      grade = "D"
    else:
      grade = "F"

    print ("Average Mark of student {:2d} = {:0.2f}, grade is {:1s}.".format(students,ave,grade) )

    math_score += m
    physics_score += p

    yes = input("Any more students? (Y or N): ")
    cont = yes == "Y" or yes == "y"  # determine if to continue

m_ave = math_score/students
p_ave = physics_score/students

print("Class average: Maths {:0.2f}, Physics {:0.2f}".format(m_ave, p_ave))
print("The overall average: {:0.2f}". format((m_ave+p_ave)/2))