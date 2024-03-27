from csv import DictReader, DictWriter

with open('students.csv') as file:
    headers = ['id', 'Name', 'titleProject_id', 'class', 'score']
    data = list(DictReader(file, delimiter=','))

count = 0
summa = 0
for student in data:
    if student['Name'].startswith('Хадаров Владимир'):
        print(f'Ты получил: {student["score"]}, за проект - {student["titleProject_id"]}')
    if student["score"] != 'None':
        count += 1
        summa += int(student["score"])

average = round(summa / count, 3)

for student in data:
    if student["score"] == 'None':
        student["score"] = average

with open('student_new.csv', 'w') as file:
    writer = DictWriter(file, delimiter=',', fieldnames=headers)

    writer.writeheader()
    writer.writerows(data)
