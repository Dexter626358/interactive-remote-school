import os.path
from group_data_provider import show_groupmates as sg
from data_file import open_data_user as od
from import_schedule_txt import import_data as imp_sch
from view_schedule import view_schedule as vs
from student import show_smarts as show_marks
from logger_action import logger_action as log
from logger_action import get_now_date as date
from check_user_input import cheats_date as cheats
from check_user_input import check_input_date as check_date
from color_out_text import out_white as white
from color_out_text import out_yellow as yellow
from color_out_text import out_red as red


def show_marks(data_user: list):
    if os.path.isfile('class_registr.txt'):
        with open('class_registr.txt', 'r', encoding='utf-8') as file:
            marks = [marks.split(';') for marks in file.read().splitlines()]
            print("\nОценки успешно выгружены из: class_registr.txt!")
    else:
        print('\nОшибка, база данных отсутствует!')
        return False
    while True:
        teacher_subject = data_user[7]
        print("\n Меню оценок")
        print('1. Показать все оценки по моему предмету')
        print('2. Показать оценки группы по моему предмету')
        print('3. Изменить оценку студента')
        print('4. Сохранить изменения оценок')
        print('5. Вернуть в главное меню преподавателя.')
        teacher_click = input("\n Выберите пункт меню: ").strip()
        if teacher_click == '1':
            for i in marks:
                if i[5] == teacher_subject:
                    result = i[0] + " " + i[2] + " " + i[3] + " " + i[4] + '-' + i[6]
                    print(result)
            log(f'Учитель по предмету {teacher_subject}, {data_user[3]} {data_user[4]} посмотрел все оценки групп')
        elif teacher_click == '2':
            group_number = input("Введите номер группы: ").strip()
            list_group_user = [i for i in marks if i[1] == group_number]
            if list_group_user:
                print()
                for i in marks:
                    if i[1] == group_number and i[5] == teacher_subject:
                        result = i[0] + " " + i[2] + " " + i[3] + " " + i[4] + '-' + i[6]
                        print(result)
                log(f'Учитель по предмету {teacher_subject}, {data_user[3]} {data_user[4]} посмотрел оценки'
                    f' {group_number}-ой группы')
            else:
                print(red('\nТакой группы нет в нашей школе.'))
                log(f'Учитель по предмету {teacher_subject}, {data_user[3]} {data_user[4]} неверно указал номер группы')
                white('')
                continue
        elif teacher_click == '3':
            group_number = input("Введите номер группы: ").strip()
            list_groupe_user = [i for i in marks if i[1] == group_number]
            if list_groupe_user:
                print()
                secured_lst = []
                for i in marks:
                    if i[1] == group_number and i[5] == teacher_subject:
                        result = i[0] + " " + i[2] + " " + i[3] + " " + i[4] + '-' + i[6]
                        secured_lst.append(i[0])
                        print(result)
                student_id = input("Введите ID студента ( число перед фамилией )    оценку которого хотите изменить: ")
                while student_id not in secured_lst:
                    print(yellow('Неверно выбран ID, повтырите попытку!'))
                    white('')
                    student_id = input("Введите ID студента ( число перед   фамилией ) оценку которого хотите изменить: ").strip()
                new_mark = input("Введите цифрой новую оценку: ").strip()
                if new_mark == '5':
                    new_mark = '5(отлично)'
                elif new_mark == '4':
                    new_mark = '4(хорошо)'
                elif new_mark == '3':
                    new_mark = '3(удовлетворительно)'
                elif new_mark == '2':
                    new_mark = '2(неуд)'
                else:
                    print('Некорректный ввод. Возврат в главное меню')
                    continue
                for i in marks:
                    if i[0] == student_id and i[5] == teacher_subject:
                        i[6] = new_mark
                        break
                print(f"Оценка ученика с логином: {student_id} успешно изменена.")
                log(f'Учитель по предмету {teacher_subject}, {data_user[3]} {data_user[4]} изменил оценку студенту '
                    f'ID - {student_id} на {new_mark}')
            else:
                print(red('\nТакой группы нет в нашей школе.'))
                log(f'Учитель по предмету {teacher_subject}, {data_user[3]} {data_user[4]} неверно указал номер группы')
                white('')
                continue
        elif teacher_click == '4':
            with open('class_registr.txt', 'w', encoding='utf-8') as file:
                for i in range(len(marks)):
                    if i != 0:
                        file.write('\n')
                    for j in range(len(marks[i])):
                        if j == 6:
                            file.write(str(marks[i][j]))
                        else:
                            file.write(str(marks[i][j]) + ';')
            log(f'Учитель по предмету {teacher_subject}, {data_user[3]} {data_user[4]} сохранил измения в базе оценок')
        elif teacher_click == '5':
            break
        else:
            print('Нет такого пункта, повторите выбор.')
            continue


def show_schedule(data: list, data2: list, user: list):
    day_ = None
    while True:
        print('\n1.Посмотреть расписание на весь месяц.')
        print('2.Посмотреть расписание на текущий день.')
        print('3.Посмотреть расписание на определенный день.')
        print('4.Вернуться в главное меню преподавателя.')
        teacher_choose = input('\nВаш выбор: ').strip()
        if teacher_choose == '1':
            print('Расписание на сентябрь.')
            searchable_group = input("Введите номер нужной группы: ").strip()
            groupe_list = [i for i in data2 if i[7] == searchable_group]
            if groupe_list:
                vs(data, searchable_group)
            else:
                print('\nТакой группы нет в нашей школе.')
                continue
            log(f'Учитель по предмету {user[7]}, {user[3]} {user[4]} посмотрел расписание')
        elif teacher_choose == '2':
            print('Расписание на сентябрь.')
            searchable_group = input("Введите номер нужной группы: ").strip()
            groupe_list = [i for i in data2 if i[7] == searchable_group]
            if groupe_list:
                day_ = cheats(date())
                vs(data, searchable_group, day_)
                log(f'Учитель по предмету {user[7]}, {user[3]} {user[4]} посмотрел расписание')
                continue
            else:
                print('\nТакой группы нет в нашей школе.')
                continue
        elif teacher_choose == '3':
            select_teacher = input('Вывести расписание для группы -> 1 или общее -> 2 ? \n: ')
            if select_teacher == '1':
                searchable_group = input("Введите номер нужной группы: ").strip()
                groupe_list = [i for i in data2 if i[7] == searchable_group]
                if groupe_list:
                    day_ = input('Введите дату через пробел "dd mm YYYY": ')\
                            .strip().replace(' ', '.')
                    if check_date(day_):
                        day_ = cheats(day_)
                        print()
                        vs(data, searchable_group, day_)
                        log(f'посмотрел расписание для группы: "{searchable_group}" на {day_} ')
                        continue
                    else:
                        yellow('\nВы ввели дату в неверном формате.')
                        white('')
                        log(f'пытался посмотреть расписание для группы: "\      {searchable_group}" на {day_} ')
                        continue
                else:
                    print('\nТакой группы нет в нашей школе.')
                    continue
            elif select_teacher == '2':
                day_ = input('Введите дату через пробел "dd mm YYYY": ')\
                            .strip().replace(' ', '.')
                if check_date(day_):
                    day_ = cheats(day_)
                    print()
                    vs(data, False, day_)
                    log(f'посмотрел общее расписание на день: {day_} ')
                    continue
                else:
                    yellow('\nВы ввели дату в неверном формате.')
                    white('')
                    log(f'пытался посмотреть расписание для группы: "\     {searchable_group}" на {day_} ')
                    continue
            else:
                print('неверный ввод.')
        elif teacher_choose == '4':
            log('вышел в главное меню.')
            break
        else:
            print(red('\nНеверная команда, повторите выбор.'))
            white('')
            continue


def teacher_menu(data: list, user: list):
    while True:
        print(f'\nАккаунт: {user[3]} {user[4]} ')
        print(f'Предмет: {user[7]}')
        print('\nMenu:')
        print('1. Посмотреть список студентов')
        print('2. Успеваемость студентов')
        print('3. Расписание студентов')
        print('4. Просмотр и редактирование ДЗ')
        print('5. Выйти из аккаунта.')
        if os.path.isfile('data_users.txt'):
            data = od('data_users.txt')
            teacher_click = input("\nВведите нужный пункт: ")
            if teacher_click == '1':
                searchable_group = input("Введите номер группы: ")
                groupe_list = [i for i in data if i[7] == searchable_group]
                if groupe_list:
                    print()
                    sg(data, searchable_group)
                    log(f'Учитель по предмету {user[7]}, {user[3]} {user[4]} посмотрел список студентов')
                else:
                    print(red('\nТакой группы нет в нашей школе.'))
                    white('')
                    continue
            elif teacher_click == '2':
                show_marks(user)
                log(f'Учитель по предмету {user[7]}, {user[3]} {user[4]} зашел в меню оценок')
            elif teacher_click == '3':
                sch_list = imp_sch('data_schedule.txt')
                show_schedule(sch_list, data, user)
                log(f'Учитель по предмету {user[7]}, {user[3]} {user[4]} зашел в меню расписания')
            elif teacher_click == '4':
                homework_menu(user)
                log(f'Учитель по предмету {user[7]}, {user[3]} {user[4]} зашел в меню ДЗ')
            elif teacher_click == '5':
                return user.clear()
            else:
                print(red('\nНет такого пункта. Выберите из menu.'))
                white('')
        else:
            print(red('Нет файла "data_users.txt"'))
            white('')
            return user.clear()


def homework_menu(user: list):
    with open('homework.txt', 'r', encoding='utf-8') as file:
        homeworks = [homework.split(';') for homework in file.readlines()]
    teacher_subject = user[7]
    while True:
        print('1. Посмотреть все домашнее задание для выбранной группы')
        print('2. Задать группе домашнее задание')
        print('3. Сохранить изменения в файле ДЗ')
        print('4. Выход')
        teacher_click = input("Введите пункт меню: ").strip()
        if teacher_click == '1':
            searchable_group = input("Введите номер группы: ").strip()
            if searchable_group != '10' and searchable_group != '20' and searchable_group != '30':
                print(red("Нет такой группы - повторите попытку!"))
                white('')
                break
            for homework in homeworks:
                if homework[0] == searchable_group and homework[1] == teacher_subject:
                    print(f'{homework[1]} - {homework[2][0:-1]}')
            log(f'Учитель по предмету {user[7]}, {user[3]} {user[4]} посмотрел ДЗ группы:{searchable_group}')
        elif teacher_click == '2':
            searchable_group = input("Введите номер группы: ").strip()
            if searchable_group != '10' and searchable_group != '20' and searchable_group != '30':
                print(red("Нет такой группы - повторите попытку!"))
                white('')
                break
            added_homework = []
            hw_string = input("Напишите домашнее задание для группы: ")
            added_homework = [searchable_group, user[7], hw_string]
            homeworks.append(added_homework)
            log(f'Учитель по предмету {user[7]}, {user[3]} {user[4]} добавил ДЗ группе:{searchable_group}')
        elif teacher_click == '3':
            with open('test_hw.txt', 'w', encoding='utf-8') as file:
                for i in range(len(homeworks)):
                    for j in range(len(homeworks[i])):
                        if j == 2:
                            file.write(str(homeworks[i][j]))
                        else:
                            file.write(str(homeworks[i][j]) + ';')
            log(f'Учитель по предмету {user[7]}, {user[3]} {user[4]} сохранил изменения в файле ДЗ')
        elif teacher_click == '4':
            log(f'Учитель по предмету {user[7]}, {user[3]} {user[4]} вышел из меню ДЗ')
            break
        else:
            print(red("Нет такого пункта меню"))
            white('')

