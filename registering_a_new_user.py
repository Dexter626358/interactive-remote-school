# Данный блок производит регистрацию данных нового пользователя.

from check_user_input import chek_use_inpt as chek


def registering_a_new_user():
    new_user = [] * 8
    user_full_name = None
    new_login = None
    new_password = None
    status = None
    discription = None
    groupe = None
    count = 3
    while count > 0:
        user_full_name = chek(4)
        if user_full_name:
            new_login = chek(5)
            if new_login:
                new_password = input('Придумайте ваш пароль: ').strip()
                status = chek(6)
                if status:
                    discription = input('Напишите о себе 2 слова: ')
                    if status == 1:
                        groupe = '1'
                    else:
                        groupe = chek(7)
                        if groupe:
                            new_user.append(new_login)
                            new_user.append(new_password)
                            new_user.extend(user_full_name)
                            new_user.append(status)
                            new_user.append(discription)
                            new_user.append(groupe)
                        else:
                            count -= 1
                            if count > 0:
                                print(\
                                f'Начнем с начала. Осталось попыток: {count}')
                            continue
                        return new_user
                else:
                    count -= 1
                    if count > 0:
                        print(f'Начнем с начала. Осталось попыток{count}')
                    continue
            else:
                count -= 1
                if count > 0:
                    print(f'Начнем с начала. Осталось попыто{count}')
                continue
        else:
            count -= 1
            if count > 0:
                print(f'Начнем с начала. Осталось попыт{count}')
            continue
    else:
        print('Попытки исчерпаны, позовите взрослого человека, он поможет зарегистрироваться =)')
        return False
