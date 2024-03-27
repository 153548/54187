from csv import DictReader

with open('students.csv') as file:
    headers = ['id', 'Name', 'titleProject_id', 'class', 'score']
    data = list(DictReader(file, delimiter=','))


def get_info(titleproject_id):
    for student in data:
        if student['titleProject_id'] == titleproject_id:
            print(f"Проект № {student['titleProject_id']} делал: "
                  f"{student['Name'].split()[1][0]}. {student['Name'].split()[0]}"
                  f" он(а) получил(а) оценку - {student['score']}.")
            return True
        if titleproject_id == 'СТОП':
            return False

    print('Ничего не найдено.')
    return True


flag = True
while flag:
    titleProject_id = input()
    flag = get_info(titleProject_id)
