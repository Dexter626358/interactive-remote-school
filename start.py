# Данный блок осуществляет авторизацию пользователя в системе.

def open_data_user(path):
    list_data = []
    with open(path, 'r', encoding='utf-8') as data:
        line = data.readlines()
        for i in line:
            list_data.append(i.replace('\n', '').split(';'))
    return list_data


def chek_use_inpt(flag, user = None):
    count_ = 0
    login = None
    while True:
        if flag == 1 and count_ < 5:
            input_ = input('выберете действие: ').strip()
        elif flag == 2 and count_ < 5:
            input_ = input('Введите ваш login: ').strip()
        elif flag == 3 and count_ < 5:
            input_ = input('Введите ваш пароль: ').strip()
        else:
            print('\nвы превысили количество попыток.\n')
            return False
        try:
            if flag == 1:
                if input_ == '1' or '2':
                    return input_
                else:
                    raise ValueError
            if flag == 2:
                if 0 < len(input_) < 10:
                    login = list(filter(lambda x: x[0] == input_, user))
                    if login:
                        return input_
                    else:
                        ValueError
                else:
                    raise ValueError
            if flag == 3:
                if input_ == user[1]:
                    print(f'Пароль принят. Рады вас приветствовать {user[2]}  {user [3]} !')
                    return input_
                else:
                    raise ValueError
        except ValueError:
            if flag == 1:
                print('Введите число соответстветствующее пункту меню.')
                count_ += 1
            if flag == 2:
                print('Такого логина в базе нет.')
                count_ += 1
            if flag == 3:
                print('Вы ввели неверный пароль. Попробуйте еще раз.')
                count_ += 1
            continue





def start():
    print('Вас приветствует интерактивный помошник школы!')
    while True:
        print('Для продолжения выберите действие \
            \n1. Ввести логин \n2. Выход')
        select_ = None
        user_list = None
        list_data = open_data_user('data_users.txt')
        select_ = chek_use_inpt(1)
        if select_ == '1':
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
        elif select_ == '2':
            return print('Программа завершена')


start()
