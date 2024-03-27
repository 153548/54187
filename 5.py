from csv import DictReader, DictWriter

with open('students.csv') as file:
    headers = ['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password']
    data = list(DictReader(file, delimiter=','))


def get_hash(name):
    p = 67
    m = 10 ** 9 + 9
    hash = 0
    for index in range(len(name)):
        hash += ord(name[index]) * p ** index

    return hash % m


for student in data:
    student['id'] = get_hash(student['Name'])

with open('students_with_hash.csv', 'w') as file:
    writer = DictWriter(file, fieldnames=headers, delimiter=',')

    writer.writeheader()
    writer.writerows(data)
