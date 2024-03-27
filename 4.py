from csv import DictReader, DictWriter
import string
from random import randint
with open('students.csv') as file:
    headers = ['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password']
    data = list(DictReader(file, delimiter=','))

def get_login(name):
    second, first, third = name.split()
    return f'{second}_{first[0]}{third[0]}'

def get_password():
    digit_flag = False
    lower_case_flag = False
    upper_case_flag = False
    alphabet = string.ascii_letters + string.digits
    password = ''
    for i in range(8):
        symbol = alphabet[randint(0, len(alphabet)-1)]
        if symbol in string.digits:
            digit_flag = True
        elif symbol in string.ascii_lowercase:
            lower_case_flag = True
        elif symbol in string.ascii_uppercase:
            upper_case_flag = True
        password += symbol
    if upper_case_flag and lower_case_flag and digit_flag:
        return password
    else:
        return get_password()

for student in data:
    student['login'] = get_login(student['Name'])
    student['password'] = get_password()

with open(' students_password.csv', 'w') as file:
    writer = DictWriter(file, fieldnames=headers, delimiter=',')

    writer.writeheader()
    writer.writerows(data)

