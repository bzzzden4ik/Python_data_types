students = [
    {"name": "Alice", "grades": [5, 4, 5, 3]},
    {"name": "Bob", "grades": [4, 4, 4, 5]},
    {"name": "Charlie", "grades": [5, 5, 5, 5]},
]

average_grades = {
    student["name"]: sum(student["grades"]) / len(student["grades"])
    for student in students
}

best_student = ''
best_value = 0

for name, avg_grade in average_grades.items():
    if avg_grade > best_value:
        best_value = avg_grade
        best_student = name

print(best_student)
