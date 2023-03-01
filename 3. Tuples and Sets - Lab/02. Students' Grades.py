number = int(input())
students_grade = {}

for i in range(number):
    person, grade = input().split()
    if person not in students_grade:
        students_grade[person] = []
    students_grade[person].append(float(grade))

# print(students_grade)
# {'Peter': [5.2, 3.2], 'Mark': [5.5, 2.5, 3.46], 'Alex': [2.0, 3.0]}

for student, grades in students_grade.items():
    grades_list = [str(f"{i:.2f}") for i in grades]
    average_grades = sum(grades) / len(grades)
    print(f"{student} -> {' '.join(grades_list)} (avg: {average_grades:.2f})")

# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00
