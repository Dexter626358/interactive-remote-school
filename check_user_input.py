# Данный блок проверяет любой ввод пользователя на стадии шагов авторизации \
# и регистрации нового пользователя.

import re
from logger_action import logger_action as log
from color_out_text import out_red as red
from color_out_text import out_white as white
from color_out_text import out_yellow as yellow


def check_chars_fullname(x):
    reg = re.search(r'\D{2,20} \D{2,20} \D{2,20}', x)
    return True if reg else False


def check_new_login(x):
    reg = re.search(r'^\w{2,20}$', x)
    return True if reg else False


def chek_use_inpt(flag, user = None):
    count_ = 5
    login = None
    while True:
        if flag == 1 and count_ > 0:
            input_ = input('\nвыберете действие: ').strip()
        elif flag == 2 and count_ > 0:
            input_ = input('\nВведите ваш login: ').strip()
        elif flag == 3 and count_ > 0:
            input_ = input('\nВведите ваш пароль: ').strip()
        elif flag == 4 and count_ > 0:
            input_ = input('\nВведите ваше полное имя(ФИО) через пробел\n: ')
        elif flag == 5 and count_ > 0:
            input_ = input('\nПридумайте ваш login(всего 2-20 символов)\nэто: буквы,цифры и "_"): ').strip()
        elif flag == 6 and count_ > 0:
            input_ = input('\nНапишите вы студент или учитель: ')
        elif flag == 7 and count_ > 0:
            input_ = input('\nВыберите в какой вы учебной группе из списка:\n1. 30-я группа \n2.20-я группа \n3.10-я группа \nваш выбор: ')
        else:
            red('\nвы превысили количество попыток.\n')
            white('')
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
                        \nРады вас приветствовать, {user[2]} {user [3]} {user [4]} !')
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
                    if not filter(lambda x: x[0] == input_, user):
                        return input_
                    else:
                        raise NameError
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
                yellow('Введите число соответстветствующее пункту меню.')
            if flag == 2:
                yellow('Такого логина в базе нет.')
            if flag == 3:
                yellow('Вы ввели неверный пароль. Попробуйте еще раз.')
            if flag == 4:
                yellow('Вы ввели неверный формат. Попробуйте еще раз.')
            if flag == 5:
                yellow('Вы ввели неверный формат. Попробуйте еще раз.')
            if flag == 6:
                yellow('Вы ввели неизвестное слово. Попробуйте еще раз.')
            if flag == 7:
                yellow('Выберите вашу группу из списка.')
            count_ -= 1
            if count_ > 0:
                print(f'\nОсталось {count_} попыток.')
                white('')
            continue
        except NameError:
            if flag == 5:
                yellow('\nэтот логин уже занят, придумайте другой.')
            count_ -= 1
            if count_ > 0:
                print(f'Осталось {count_} попыток.')
                white('')
            continue


