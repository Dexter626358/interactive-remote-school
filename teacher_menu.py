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


def show_marks(data_user: list):
    if os.path.isfile('class_registr.txt'):
        with open('class_registr.txt', 'r', encoding='utf-8') as file:
            marks = [marks.split(';') for marks in file.read().splitlines()]
            print("\nОценки успешно выгружены из: class_registr.txt!")
    else:
        print('\nОшибка, база данных отсутствует!')
        return False
    while True:
        teacher_subject = 'Математика'
        print("\n Меню оценок")
        print('1. Показать все оценки по моему предмету')
        print('2. Показать оценки группы по моему предмету')
        print('3. Изменить оценку студента')
        print('4. Сохранить изменения оценок')
        print('5.Вернуть в главное меню преподавателя.')
        teacher_click = input("\n Выберите пункт меню: ").strip()
        if teacher_click == '1':
            for i in marks:
                if i[5] == teacher_subject:
                    result = i[0] + " " + i[2] + " " + i[3] + " " + i[4] + '-' + i[6]
                    print(result)
        elif teacher_click == '2':
            group_number = input("Введите номер группы: ").strip()
            list_groupe_user = [i for i in data_user if i[7] == group_number]
            if list_groupe_user:
                print()
                for i in marks:
                    if i[1] == group_number and i[5] == teacher_subject:
                        result = i[0] + " " + i[2] + " " + i[3] + " " + i[4] + '-'  + i[6]
                        print(result)
            else:
                print('\nТакой группы нет в нашей школе.')
                continue
        elif teacher_click == '3':
            group_number = input("Введите номер группы: ").strip()
            list_groupe_user = [i for i in data_user if i[7] == group_number]
            if list_groupe_user:
                print()
                secured_lst = []
                for i in marks:
                    if i[1] == group_number and i[5] == teacher_subject:
                        result = i[0] + " " + i[2] + " " + i[3] + " " + i[4] + '-'  + i[6]
                        secured_lst.append(i[0])
                        print(result)
                student_id = input("Введите ID студента ( число перед фамилией )    оценку которого хотите изменить: ")
                while student_id not in secured_lst:
                    print('Неверно выбран ID, повтырите попытку!')
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
            else:
                print('\nТакой группы нет в нашей школе.')
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
        elif teacher_click == '5':
            break
        else:
            print('Нет такого пункта, повторите выбор.')
            continue


def show_schedule(data: list, data2: list):
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
        elif teacher_choose == '2':
            print('Расписание на сентябрь.')
            searchable_group = input("Введите номер нужной группы: ").strip()
            groupe_list = [i for i in data2 if i[7] == searchable_group]
            if groupe_list:
                day_ = cheats(date())
                vs(data, searchable_group, day_)
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
                        day_ = cheats(check_date(day_))
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
                    day_ = cheats(check_date(day_))
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
            print('\nНеверная команда, повторите выбор.')
            continue


def teacher_menu(data: list, user: list):
    while True:
        print(f'\nАккаунт: {user[3]} {user[4]} ')
        print('Menu:')
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
                else:
                    print('\nТакой группы нет в нашей школе.')
                    continue
            elif teacher_click == '2':
                show_marks(data)
            elif teacher_click == '3':
                sch_list = imp_sch('data_schedule.txt')
                show_schedule(sch_list, data)
            elif teacher_click == '4':
                pass
            elif teacher_click == '5':
                return user.clear()
            else:
                print('\nНет такого пункта. Выберите из menu.')
        else:
            print('Нет файла "data_users.txt"')
            return user.clear()


#show_marks()

# teacher_menu(data)