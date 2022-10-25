# Данный блок проверяет любой ввод пользователя на стадии шагов авторизации \
# и регистрации нового пользователя.

import re
from logger_action import logger_action as log
from color_out_text import out_red as red
from color_out_text import out_white as white
from color_out_text import out_yellow as yellow
from color_out_text import out_green as green


def check_chars_fullname(x):
    reg = re.search(r'\D{2,20} \D{2,20} \D{2,20}', x)
    return True if reg else False


def check_new_login(x):
    reg = re.search(r'^\w{2,20}$', x)
    return True if reg else False


def check_name_object(x):
    match = re.search(r'^\D{5,20}$', x)
    return True if match else False


def check_input_date(x):
    math = re.search(r'^\d\d.\d\d.\d{4}$', x)
    return True if math else False

def cheats_date (x):
    math = re.sub(r'\d\d.\d\d.\d{4}', f'{x[:2]}.09.2022', x)
    return math

def check_groupe_in_data(groupe, data):
    list_group_user = [i for i in data if i[7] == groupe]
    return True if list_group_user else False


def check_groupe_in_marks(groupe, data):
    list_group_user = [i for i in data if i[1] == groupe]
    return True if list_group_user else False


def chek_use_inpt(flag, user = None):
    count_ = 5
    login = None
    action = None
    while True:
        if flag == 1 and count_ > 0:
            input_ = input('\nвыберете пункт меню: ').strip()
            action = 'пунктов меню'
        elif flag == 2 and count_ > 0:
            input_ = input('\nВведите ваш login: ').strip()
            action = 'логина'
        elif flag == 3 and count_ > 0:
            input_ = input('\nВведите ваш пароль: ').strip()
            action = 'пароля'
        elif flag == 4 and count_ > 0:
            input_ = input('\nВведите ваше полное имя(ФИО) через пробел\n: ').strip()
            action = 'полного имени нового пользователя'
        elif flag == 5 and count_ > 0:
            input_ = input('\nПридумайте ваш login(всего 2-20 символов)\nэто: буквы,цифры и "_"): ').strip()
            action = 'нового логина нового пользователя'
        elif flag == 6 and count_ > 0:
            input_ = input('\nНапишите вы студент или учитель: ').strip()
            action = 'принядлежности нового пользователя к касте'
        elif flag == 7 and count_ > 0:
            input_ = input('\nВыберите в какой вы учебной группе из списка:\n1.30-я группа \n2.20-я группа \n3.10-я группа \nваш выбор: ').strip()
            action = 'выбора своей группы'
        elif flag == 8 and count_ >0:
            input_ = input('\n Напишите название вашего предмета: ').strip()
            action = 'названия предмета своей специализации'
        else:
            log(f'превысил допустимое количество попыток ввода {action} .')
            red('\nвы превысили количество попыток.\n')
            white('')
            return False
        try:
            if flag == 1:
                if input_ == '1' or input_ == '2' or input_ == '3':
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
                    green(f'\nПароль принят. \
                        \nРады вас приветствовать, {user[2]} {user [3]} {user [4]} !')
                    white('')
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
                    key_log = list(filter(lambda x: x[0] == input_, user))
                    if not key_log:
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
            elif flag == 8:
                if check_name_object(input_):
                    return input_
                else:
                    raise NameError
        except ValueError:
            if flag == 1 and count_ == 5:
                red('\nНет такого пункта. Повторите ввод.\n')
                yellow('\nНе спешите нажимать клавиатуру, прочитите текст и')
                yellow('введите число соответстветствующее пункту меню.')
            elif flag == 1:
                yellow('введите число соответстветствующее пункту меню.')
            elif flag == 2:
                yellow('\nТакого логина в базе нет.')
            elif flag == 3:
                yellow('\nВы ввели неверный пароль. Попробуйте еще раз.')
            elif flag == 4:
                yellow('\nВы ввели неверный формат. Попробуйте еще раз.')
            elif flag == 5:
                yellow('\nВы ввели неверный формат. Попробуйте еще раз.')
            elif flag == 6:
                yellow('\nВы ввели неизвестное слово. Попробуйте еще раз.')
            elif flag == 7:
                yellow('\nВыберите вашу группу из списка.')
            count_ -= 1
            if count_ > 0:
                print(f'Осталось {count_} попыток.')
                white('')
            continue
        except NameError:
            if flag == 5:
                yellow('\nэтот логин уже занят, придумайте другой.')
            elif flag == 8:
                yellow('\nэто не похоже на название предмета.')
            count_ -= 1
            if count_ > 0:
                print(f'Осталось {count_} попыток.')
                white('')
            continue
