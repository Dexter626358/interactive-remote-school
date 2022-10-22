# Данный блок работает с файлами.

from logger_action import logger_action as log


def open_data_user(path):
    list_data = []
    with open(path, 'r', encoding='utf-8') as data:
        line = data.readlines()
        for i in line:
            i.replace(' ', '')
            list_data.append(i.replace('\n', '').split(';'))
    log(f'скачал базу из файла: {path}')
    return list_data


def add_record_new_user(base: list, new_user: list, path: str):
    base.append(new_user)
    new_user = ';'.join(new_user)
    with open(path, 'a', encoding='utf-8') as data:
        data.write(f'\n{new_user}')
    log(f'добавил нового пользователя в базу: {path}')
    return base
