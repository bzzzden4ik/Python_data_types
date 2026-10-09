data = [
    {"student": "Alice", "subject": "Math", "grade": 5},
    {"student": "Bob", "subject": "Math", "grade": 4},
    {"student": "Alice", "subject": "History", "grade": 3},
    {"student": "Bob", "subject": "History", "grade": 5},
]
result = dict()

for item in data:
    subject = item["subject"]
    student = item["student"]
    grade = item["grade"]
    
    if subject not in result:
        result[subject] = dict()
        
    result[subject][student] = grade

print(result)
