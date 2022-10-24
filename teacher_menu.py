from group_data_provider import show_groupmates as sg
from data_file import open_data_user as od
from import_schedule_txt import import_data as imp_sch
from view_schedule import view_schedule as vs
from student import show_smarts as show_marks
from logger_action import logger_action as log
from logger_action import get_now_date as date


def show_marks():
    with open('class_registr.txt', 'r', encoding='utf-8') as file:
        marks = [marks.split(';') for marks in file.read().splitlines()]
        print("Оценки успешно выгружены из class_registr.txt!")
    while True:
        teacher_subject = 'Математика'
        print("\n Меню оценок")
        print('1. Показать все оценки по моему предмету')
        print('2. Показать оценки группы по моему предмету')
        print('3. Изменить оценку студента')
        print('4. Сохранить изменения оценок')
        teacher_click = input("\n Выберите пункт меню: ")
        if teacher_click == '1':
            for i in marks:
                if i[5] == teacher_subject:
                    result = i[0] + " " + i[2] + " " + i[3] + " " + i[4] + '-' + i[6]
                    print(result)
        if teacher_click == '2':
            group_number = input("Введите номер группы: ")
            print()
            for i in marks:
                if i[1] == group_number and i[5] == teacher_subject:
                    result = i[0] + " " + i[2] + " " + i[3] + " " + i[4] + '-' + i[6]
                    print(result)
        if teacher_click == '3':
            group_number = input("Введите номер группы: ")
            print()
            secured_lst = []
            for i in marks:
                if i[1] == group_number and i[5] == teacher_subject:
                    result = i[0] + " " + i[2] + " " + i[3] + " " + i[4] + '-' + i[6]
                    secured_lst.append(i[0])
                    print(result)
            student_id = input("Введите ID студента ( число перед фамилией ) оценку которого хотите изменить: ")
            while student_id not in secured_lst:
                print('Неверно выбран ID, повтырите попытку!')
                student_id = input("Введите ID студента ( число перед фамилией ) оценку которого хотите изменить: ")
            new_mark = input("Введите цифрой новую оценку: ")
            if new_mark == '5':
                new_mark = '5(отлично)'
            if new_mark == '4':
                new_mark = '4(хорошо)'
            if new_mark == '3':
                new_mark = '3(удовлетворительно)'
            if new_mark == '2':
                new_mark = '2(неуд)'
            else:
                print('Некорректный ввод. Возврат в главное меню')
                pass
            for i in marks:
                if i[0] == student_id and i[5] == teacher_subject:
                    i[6] = new_mark
                    break
            print("Оценка успешно изменена")

        if teacher_click == '4':
            with open('test_marks.txt', 'w', encoding='utf-8') as file:
                for i in range(len(marks)):
                    if i != 0:
                        file.write('\n')
                    for j in range(len(marks[i])):
                        if j == 6:
                            file.write(str(marks[i][j]))
                        else:
                            file.write(str(marks[i][j]) + ';')








def show_schedule(data: list):
    day_ = None
    searchable_group = input("Введите номер нужной группы: ")
    while True:
        print('\n1.Посмотреть расписание на весь месяц.')
        print('2.Посмотреть расписание на текущий день.')
        print('3.Посмотреть расписание на определенный день.')
        print('4.Посмотреть расписание для другой группы.')
        print('5.Вернуть в главное меню')
        teacher_choose = input('\nВаш выбор: ')
        if teacher_choose == '1':
            print('Расписание на сентябрь.')
            vs(data, searchable_group)
        elif teacher_choose == '2':
            day_ = date().replace('10', '09')
            vs(data, searchable_group, day_)
            continue
        elif teacher_choose == '3':
            day_ = input('Введите дату через пробел "dd mm YYYY": ')\
                        .replace(' ', '.')
            vs(data, searchable_group, day_)
            continue
        elif teacher_choose == '4':
            other_group = input('\nНапишите номер группы: ')
            if other_group == data[0]['группа'] or other_group == data[1]['группа'] or other_group == data[2]['группа']:
                vs(data, other_group)
                continue
        elif teacher_choose == '5':
            log('вышел в главное меню.')
            break
        else:
            print('\nНеверная команда, повторите выбор.')
            continue



def teacher_menu(data: list, user: list):
    while True:
        print(f'\n{user[3]} {user[4]} пожаловать в меню преподавателя!')
        print('1. Посмотреть список студентов')
        print('2. Успеваемость студентов')
        print('3. Расписание студентов')
        print('4. Просмотр и редактирование ДЗ')
        teacher_click = input("\nВведите нужный пункт: ")
        if teacher_click == '1':
            searchable_group = input("Введите номер группы: ")
            print()
            sg(data, searchable_group)
        elif teacher_click == '2':
            show_marks()
        elif teacher_click == '3':
            show_schedule(sch_list)

        elif teacher_click == '4':
            pass

data = od('data_users.txt')
sch_list = imp_sch('data_schedule.txt')

#show_marks()

# teacher_menu(data)