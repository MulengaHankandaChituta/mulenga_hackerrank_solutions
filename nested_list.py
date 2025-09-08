# HackerRank Nested Lists Problem Solution
# Author: Mulenga Chituta

if __name__ == '__main__':
    students = []

    n = int(input("Enter number of students: "))  # total number of students

    for _ in range(n):
        name = input("Enter student name: ")
        score = float(input("Enter student score: "))
        students.append([name, score])

    # Extract unique scores and sort them
    scores = sorted(set(student[1] for student in students))

    # Get the second lowest score
    second_lowest = scores[1]

    # Find all students with that score, sort names alphabetically
    result = sorted([student[0] for student in students if student[1] == second_lowest])

    print("\nStudents with the second lowest score:")
    for name in result:
        print(name)
