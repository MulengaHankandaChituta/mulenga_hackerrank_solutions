from collections import namedtuple

# Read number of students
n = int(input())

# Read column names (in any order)
cols = input().split()

# Create the student namedtuple dynamically
Student = namedtuple('Student', cols)

# Read student data, sum the marks, and calculate average
total_marks = 0
for _ in range(n):
    student_data = input().split()
    student = Student(*student_data)
    total_marks += int(student.MARKS)

# Print average marks rounded to 2 decimal places
print(f"{total_marks / n:.2f}")
    
