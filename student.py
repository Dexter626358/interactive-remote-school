# Данный блок развивает собития пользователя ученик/студент.
# from genericpath import isfile
import os.path
# from unittest.mock import patch
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
from check_user_input import chits_data as chits


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
            print('Расписание на сентябрь.')
            vw_schdl(data, groupe)
            log(f'посмотрел расписание для группы:{groupe} на месяц сентябрь.')
        elif student_choose == '2' :
            day_ = date().replace('10', '09')
            vw_schdl(data, groupe, day_)
            log(f'посмотрел расписание для группы:{groupe} на {day_} ')
            continue
        elif student_choose == '3' :
            green('\nЛюбая дата сентября 2022 года.\n')
            white('')
            day_ = input('Введите дату через пробел "dd mm YYYY": ')\
                        .strip().replace(' ', '.')
            if check_date(day_):
                day_ = chits(check_date(day_))
            else:
                yellow('\nВы ввели дату в неверном формате.')
                white('')
                log(f'пытался посмотреть расписание для группы:{groupe} на {day_} ')
                continue
            print()
            vw_schdl(data, groupe, day_)
            log(f'посмотрел расписание для группы:{groupe} на {day_} ')
            continue
        elif student_choose == '4' :
            other_groupe = input('\nНапишите номер группы: ')
            if other_groupe == data[0] ['группа']or other_groupe == data[1]['группа'] or other_groupe == data[2]['группа']:
                vw_schdl(data, other_groupe)
                log(f'посмотрел расписание для группы:{other_groupe}')
                continue
            else:
                yellow('\nУ нас нет такой группы.')
                white('')
                log(f'пытался посмотреть расписание для группы:{groupe}')
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
    log(f'вошел в меню ученика под аккаунтом: {user[0]}-> {user[2]} {user[3]}.')
    while True:
        print("\nВы находитесь в личном кабинете студента")
        print("\n1. Досмотреть домашнее задание по предмету")
        print("2. Посмотреть успеваемость по предметам")
        print("3. Посмотреть расписание занятий")
        print("4. Выход")
        student_choose = input('\nВаш выбор: ')
        #student_choose = '2'
        if student_choose == '1':
            log('перешел  к просомтру домашнего задания.')
            pass
        elif student_choose == '2':
            show_smarts()
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


