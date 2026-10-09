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

best_student = max(average_grades, key=average_grades.get)

print(best_student)
