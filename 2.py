from csv import DictReader

with open('students.csv') as file:
    headers = ['id', 'Name', 'titleProject_id', 'class', 'score']
    data = list(DictReader(file, delimiter=','))

first = {'Name': "", 'score': 0}
second = {'Name': "", 'score': 0}
third = {'Name': "", 'score': 0}

for student in data:
    if not(student['class'].startswith('10')):
        continue

    if int(student['score']) > first['score']:
        third['score'] = second['score']
        second['score'] = first['score']
        first['score'] = int(student['score'])

        third['Name'] = second['Name']
        second['Name'] = first['Name']
        first['Name'] = student['Name']

    elif int(student['score']) > second['score']:
        third['score'] = second['score']
        second['score'] = int(student['score'])

        third['Name'] = second['Name']
        second['Name'] = student['Name']

    elif int(student['score']) > third['score']:
        third['score'] = int(student['score'])

        third['Name'] = student['Name']


print(f'''10 класс:
1 место: {first['Name'].split()[1][0]}. {first['Name'].split()[0]}
2 место: {second['Name'].split()[1][0]}. {second['Name'].split()[0]}
3 место: {third['Name'].split()[1][0]}. {third['Name'].split()[0]}''')
