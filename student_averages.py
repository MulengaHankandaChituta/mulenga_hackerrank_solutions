# HackerRank: Find the percentage problem solution
# Author: Mulenga Chituta

if __name__ == '__main__':
    student_marks = {}

    n = int(input("Enter number of students: "))

    for _ in range(n):
        entry = input("Enter student name and marks separated by spaces: ").split()
        name, *line = entry
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input("Enter the name of the student to query: ")

    if query_name in student_marks:
        # calculate the average
        avg = sum(student_marks[query_name]) / len(student_marks[query_name])
        # print to two decimal places
        print(f"\nAverage score for {query_name}: {avg:.2f}")
    else:
        print(f"\nStudent '{query_name}' not found.")
