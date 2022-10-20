# Данный блок осуществляет авторизацию пользователя в системе \
# и регитсрацию нового.
from registering_a_new_user import registering_a_new_user as rn
import re
# from unittest.mock import patch
# from unittest.mock import patch


def check_chars_fullname(x):
    reg = re.search(r'\D{2,20} \D{2,20} \D{2,20}', x)
    return True if reg else False


def check_new_login(x):
    reg = re.search(r'^\w{2,20}$', x)
    return True if reg else False


def open_data_user(path):
    list_data = []
    with open(path, 'r', encoding='utf-8') as data:
        line = data.readlines()
        # for i in line:
        #     list_data.append(i.replace('\n', '').split(';'))
    return [i.replase('\n', '').split() for i in line if i]


def add_record_new_user(base: list, new_user: list, path: str):
    base.append(new_user)
    new_user = ';'.join(new_user)
    with open(path, 'a', encoding='utf-8') as data:
        data.write(f'\n{new_user}')
    return base


def chek_use_inpt(flag, user = None):
    count_ = 5
    login = None
    while True:
        if flag == 1 and count_ > 0:
            input_ = input('выберете действие: ').strip()
        elif flag == 2 and count_ > 0:
            input_ = input('Введите ваш login: ').strip()
        elif flag == 3 and count_ > 0:
            input_ = input('Введите ваш пароль: ').strip()
        elif flag == 4 and count_ > 0:
            input_ = input('Введите ваше полное имя(ФИО) через пробел\n: ')
        elif flag == 5 and count_ > 0:
            input_ = input('Придумайте ваш login(всего 2-20 символов)\nэто: буквы,цифры и "_"): ').strip()
        elif flag == 6 and count_ > 0:
            input_ = input('Напишите вы студент или учитель: ')
        elif flag == 7 and count_ > 0:
            input_ = input('Выберите в какой вы учебной группе из списка:\n1. 30-я группа \n2.20-я группа \n3.10-я группа \nваш выбор: ')
        else:
            print('\nвы превысили количество попыток.\n')
            return False
        try:
            if flag == 1:
                if input_ == '1' or '2':
                    return input_
                else:
                    raise ValueError
            elif flag == 2:
                if 0 < len(input_) < 10:
                    login = list(filter(lambda x: x[0] == input_, user))
                    if login:
                        return input_
                    else:
                        ValueError
                else:
                    raise ValueError
            elif flag == 3:
                if input_ == user[1]:
                    print(f'Пароль принят. \
                        \nРады вас приветствовать {user[2]}  {user [3]} {user [4]} !')
                    return input_
                else:
                    raise ValueError
            elif flag == 4:
                if check_chars_fullname(input_):
                    return input_.strip().split()
                else:
                    raise ValueError
            elif flag == 5:
                if check_new_login(input_):
                    return input_
                else:
                    raise ValueError
            elif flag == 6:
                if input_.strip().lower() == 'студент' or 'ученик':
                    return '0'
                elif input_.strip().lower() == 'учитель' or 'преподаватель':
                    return '1'
                else:
                    raise ValueError
            elif flag == 7:
                if input_.strip().lower() == '1' or '30-я' or '30-я группа' or '30':
                    return '30'
                elif input_.strip().lower() == '2' or '20-я' or '20-я группа' or '20':
                    return '20'
                elif input_.strip().lower() == '3' or '10-я' or '10-я группа' or '10':
                    return '10'
                else:
                    raise ValueError
        except ValueError:
            if flag == 1:
                print('Введите число соответстветствующее пункту меню.')
            if flag == 2:
                print('Такого логина в базе нет.')
            if flag == 3:
                print('Вы ввели неверный пароль. Попробуйте еще раз.')
            if flag == 4:
                print('Вы ввели неверный формат. Попробуйте еще раз.')
            if flag == 5:
                print('Вы ввели неверный формат. Попробуйте еще раз.')
            if flag == 6:
                print('Вы ввели неизвестное слово. Попробуйте еще раз.')
            if flag == 7:
                print('Выберите вашу группу из списка.')
            count_ -= 1
            print(f'Осталось {count_} попыток.')
            continue


def start():
    print('Вас приветствует интерактивный помошник школы!')
    path = 'data_users.txt'
    while True:
        print('Для продолжения выберите действие:\
            \n1.Регистрация\n2.Вход\n3. Выход')
        select_ = None
        user_list = None
        list_data = open_data_user(path)
        select_ = chek_use_inpt(1)
        if select_ == '1':
            new_user = rnews()
            if new_user:
                list_data = add_record_new_user(list_data, new_user, path)
            else:
                continue
        elif select_ == '2':
            log_ = chek_use_inpt(2, list_data)
            if log_:
                user_list = [i for i in list_data if i[0] == log_]
                user_list = user_list[0]
            else:
                continue
            password = chek_use_inpt(3, user_list)
            if password:
                return user_list
            else:
                continue
        elif select_ == '3':
            return print('Программа завершена')


start()
