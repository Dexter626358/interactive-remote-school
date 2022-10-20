def show_smarts():
    with open('class_registr.txt', 'r', encoding='utf-8') as file:
        smarts = [smart.split(';') for smart in file.readlines()]
    print("1. Показать оценки за определенную дату")
    print("2. Показать оценки по предмету")
    print("3. Показать все оценки")
    student_smarts = input()
    if student_smarts == '1':
        print('Введите дату в формате dd-mm-yyyy')
        data = input()
        #data = '20-10-2022'
        data_smarts = [smart for smart in smarts if data in smart]
        if data_smarts:
            for data_smart in data_smarts:
                print(f'{data_smart[1]} {data_smart[5]} {data_smart[6]}')
        else:
            print('Нет данных')
    elif student_smarts == '2':
        print('Введите название предмета')
        subject = input().lower()
        #subject = 'химия'
        subject_smarts = [smart for smart in smarts if subject in smart]
        if subject_smarts:
            for subject_smart in subject_smarts:
                print(f'{subject_smart[1]} {subject_smart[5]} {subject_smart[6]}')
        else:
            print('Нет данных')
    elif student_smarts == '3':
        surname_smarts = [smart for smart in smarts]
        if surname_smarts:
                for surname_smart in surname_smarts:
                    print(f'{surname_smart[1]} {surname_smart[5]} {surname_smart[6]}')
        else:
            print('Нет данных')
    else:
        print("Вы ввели что-то не то. Попробуйте снова")
        show_smarts()

def show_home_work():
    pass

def show_scadule():

print("Вы находитесь в личном кабинете студента")
print("1. Досмотреть домашнее задание по предмету")
print("2. Посмотреть успеваемость по предметам")
print("3. Посмотреть расписание занятий")
student_choose = input()
#student_choose = '2'
if student_choose == '1':
     pass
elif student_choose == '2':
    show_smarts()
elif student_choose == '3':
     pass
else:
     print("Вы ввели что-то не то. Попробуйте снова")







