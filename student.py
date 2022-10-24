# Данный блок развивает собития пользователя ученик/студент.

import os.path
from import_schedule_txt import import_data as schedule
from view_schedule import view_schedule as vw_schdl
from logger_action import logger_action as log
from logger_action import get_now_date as date
from color_out_text import out_blue as blue
from color_out_text import out_white as white
from color_out_text import out_yellow as yellow
from color_out_text import out_red as red
from color_out_text import out_green as green
from check_user_input import check_input_date as check_date
from check_user_input import cheats_date as cheats


def show_smarts(user: list):
    with open('class_registr.txt', 'r', encoding='utf-8') as file:
        smarts = [smart.split(';') for smart in file.readlines()]
    user = user[0]
    while True:
        print("1. Показать оценки по предмету")
        print("2. Показать все оценки")
        print("3. Вернуться в меню студента")
        student_smarts = input()
        if student_smarts == '1':
            print('Введите название предмета')
            subject = input().lower()
            if subject in ['химия', 'биология', 'информатика', 'математика', 'русский язык', 'литература', 'история', 'физика']:
                flag_subj = False
                for smart in smarts:
                    if smart[0] == user and smart[5].lower() == subject:
                        flag_subj = True
                        print(f'{smart[6][0:-1]}')
                print()
                if flag_subj == False:
                    print("Оценок нет")
            else:
                print('Такой предмет отсутствует')
                print()
        elif student_smarts == '2':
            for smart in smarts:
                if smart[0] == user:
                    print(f'{smart[5]} - {smart[6][0:-1]}')
            print()
        elif student_smarts == '3':
            break
        else:
            print("Вы ввели что-то не то. Попробуйте снова")


def show_home_work(data: list, user: list):
    with open('homework.txt', 'r', encoding='utf-8') as file:
        homeworks = [homework.split(';') for homework in file.readlines()]
    groupe = user[7]
    while True:
        print(f'1. Посмотреть все домашнее задание для {groupe} группы')
        print('2. Посмотреть домашнее задание по предмету')
        print('3. Выход')
        student_choose = input('\nВаш выбор: ')
        print()
        if student_choose == '1':
            for homework in homeworks:
                if homework[0] == groupe:
                    print(f'{homework[1]} - {homework[2][0:-1]}')
            print()
        elif student_choose == '2':
            print('Введите название предмета:')
            subject = input().lower()
            if subject in ['химия', 'биология', 'информатика', 'математика', 'русский язык', 'литература', 'физика']:
                for homework in homeworks:
                    if homework[0] == groupe and homework[1] == subject:
                        print(f'{homework[2][0:-1]}')
                print()
            else:
                print('По этому предмету домашнее задение отсуствует')
                print()

        elif student_choose == '3':
            break
        else:
            print("Вы ввели некоректное значение. Попробуйте снова.")


def show_scadule(data: list, user: list):
    groupe = user[7]
    day_ = None
    while True:
        print('\n1.Посмотреть расписание на весь месяц.')
        print('2.Посмотреть расписание на текущий день.')
        print('3.Посмотреть расписание на определенный день.')
        print('4.Посмотреть расписание для другой группы.')
        print('5.Вернуть в главное меню студента')
        student_choose = input('\nВаш выбор: ')
        print()
        if student_choose == '1':
            blue('Расписание на сентябрь.')
            white('')
            vw_schdl(data, groupe)
            log(f'посмотрел расписание для группы: "{groupe}" на месяц сентябрь.')
        elif student_choose == '2':
            day_ = cheats(date())
            vw_schdl(data, groupe, day_)
            log(f'посмотрел расписание для группы: "{groupe}" на {day_} ')
            continue
        elif student_choose == '3' :
            green('\nЛюбая дата сентября 2022 года.\n')
            white('')
            day_ = input('Введите дату через пробел "dd mm YYYY": ')\
                        .strip().replace(' ', '.')
            if check_date(day_):
                day_ = cheats(check_date(day_))
            else:
                yellow('\nВы ввели дату в неверном формате.')
                white('')
                log(f'пытался посмотреть расписание для группы: "{groupe}" на {day_} ')
                continue
            print()
            vw_schdl(data, groupe, day_)
            log(f'посмотрел расписание для группы: "{groupe}" на {day_} ')
            continue
        elif student_choose == '4' :
            other_groupe = input('\nНапишите номер группы: ')
            if other_groupe == data[0]['группа'] or other_groupe == data[1]['группа'] or other_groupe == data[2]['группа']:
                vw_schdl(data, other_groupe)
                log(f'посмотрел расписание для группы: "{other_groupe}"')
                continue
            else:
                yellow('\nУ нас нет такой группы.')
                white('')
                log(f'пытался посмотреть расписание для группы: "{other_groupe}"')
                continue
        elif student_choose == '5':
            log('вернулся в главное меню студента.')
            break
        else:
            red('\nНеверная команда, повторите выбор.')
            white('')
            log('ошибся с выбором пункта меню.')
            continue


def user_student_start(data: list, user: list):
    patch_schedule = 'data_schedule.txt'
    log(f'Вошел в меню ученика под аккаунтом: {user[0]}-> {user[2]} {user[3]}.')
    while True:
        print("\nВы находитесь в личном кабинете студента")
        print("\n1. Досмотреть домашнее задание по предмету")
        print("2. Посмотреть успеваемость по предметам")
        print("3. Посмотреть расписание занятий")
        print("4. Выход из аккаунта")
        student_choose = input('\nВаш выбор: ')
        if student_choose == '1':
            log('перешел  к просмотру домашнего задания.')
            show_home_work(data, user)
        elif student_choose == '2':
            show_smarts(user)
            log('перешел  к просомтру успеваемости.')
        elif student_choose == '3':
            if os.path.isfile(patch_schedule):
                schedule_list = schedule(patch_schedule)
                show_scadule(schedule_list, user)
                log('перешел  к просомтру расписания.')
            else:
                red('\nОшибка. Такого файла нет.')
                white('')
                continue
        elif student_choose == '4':
            log(f'вышел из аккаунта: {user[0]} .')
            user.clear()
            return user
        else:
            log(f'ошибся с пунктом меню ученика.')
            print("Вы ввели что-то не то. Попробуйте снова")
            continue
