from group_data_provider import show_groupmates as sg
from data_file import open_data_user as od
from import_schedule_txt import import_data as imp_sch
from view_schedule import view_schedule as vs
from student import show_smarts as show_marks
from logger_action import logger_action as log
from logger_action import get_now_date as date




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



def teacher_menu(data: list):
    while True:
        print('\nДобро пожаловать в меню преподавателя!')
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
            show_schedule(sch_list, )

        elif teacher_click == '4':
            pass

data = od('data_users.txt')
sch_list = imp_sch('data_schedule.txt')

teacher_menu(data)