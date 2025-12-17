# program to demonstrate the zip function

# read number of students and subjects
n, x = map(int, input().split())

# store marks for each subject
marks = []
for _ in  range(x):
    subject_marks = list(map(float, input().split()))
    marks.append(subject_marks)

# calculate and print averages for each student
for student_marks in zip(*marks):
    average = sum(student_marks) / x
    print(f"{average:.1f}")
