# https://www.hackerrank.com/challenges/py-collections-namedtuple/

from collections import namedtuple

# Read number of students and column header
num_students = int(input())
columns = input().split()
Student = namedtuple('Student', columns)

# Create list of all students
students = []

# Read student data
for student in range(num_students):
    student_data = input().split()
    # Create a namedtuple out of the student and their data and append to student list 
    students.append(Student(*student_data))

# Get index of the MARKS field    
marks_index = columns.index('MARKS')
# Sum all MARKS data in the list using list comprehension
total_marks = sum(int(student[marks_index]) for student in students)
average_marks = total_marks / num_students

# Pritn average marks to two decimal places using stirng formatting
print(f"{average_marks:.2f}")