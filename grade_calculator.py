
#---------------PROGRAM 4---------------

name = input("Enter student name: ")
student_class = input("Enter class: ")
section = input("Enter section: ")

mrk1 = int(input("Enter marks of Subject 1: "))
mrk2 = int(input("Enter marks of Subject 2: "))
mrk3 = int(input("Enter marks of Subject 3: "))
mrk4 = int(input("Enter marks of Subject 4: "))
mrk5 = int(input("Enter marks of Subject 5: "))

total = mrk1 + mrk2 + mrk3 + mrk4 + mrk5
average = total / 5

if average >= 90:
    grade = "Outstanding"
elif average >= 80:
    grade = "Very Good"
elif average >= 60:
    grade = "Good"
elif average >= 50:
    grade = "Fair"
else:
    grade = "Participation"

print("----- STUDENT RESULT -----")
print("Name:", name)
print("Class:", student_class)
print("Section:", section)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)

#----------------END---------------