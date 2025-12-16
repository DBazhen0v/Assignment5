processed_results = [
{'student_name': 'Анна', 'score': 91, 'passed': True},
{'student_name': 'Богдан', 'score': 58, 'passed': False},
{'student_name': 'Вікторія', 'score': 75, 'passed': True},
{'student_name': 'Григорій', 'score': 45, 'passed': False}
    ]
successful_students = []

for student in processed_results:
    if student["passed"] == True:
        successful_students.append(student)

print(successful_students)
print("Склали іспит:", len(successful_students))

