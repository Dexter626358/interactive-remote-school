# Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

# Препод\студент
# Студент: ФИО, список отметок, по какому предмету, дз
# Препод: список студентов по группам, добавление дз

# Функции:
# 1. Меню
# 2. База пользователей ('login; password; surname; name; status; description')
# 3. База предметов("subject_name; login; home_task")
# 4. Таблицы со студентами
# 5. Интерфейс студента
# 6. Интерфейс препода

# Интерфейс студента: на вход логин
# 9. Выйти
# 1. Спросить предмет -> Выдать дз

# Интерфейс преподавателя: на вход логин
# 9. Выйти
# 1. Спросить группу
# 2. Спросить предмет
# 3. Добавить\изменить дз

# Меню:
# 1. Авторизация(data_read) -> Студент\Преподаватль -> Открыть соответсвующий интерфейс -> "Пользователь не найден"

# Методы:
# UI
#     data input
# data read
# data write


def open_data_user(path):
    list_data = []
    with open(path, 'r', encoding='utf-8') as data:
        line = data.readlines()
        for i in line:
            list_data.append(i.replace('\n', '').split(';'))
    print(list_data)
    return list_data



def start():
    print('Вас приветствует интерактивный помошник школы!')
    print('Для продолжения выберите действие \
        \n1. Ввести логин \n2. Выход')
    select_ = None
    user_list = None
    select_ = int(input('выберете действие: '))
    if select_ == 1:
        log_ = input('введите ваш логин: ')
        list_data = open_data_user('data_users.txt')
        user_list = [i for i in list_data if i[0] == log_]
        return user_list
    elif select_ == 2:
        return False

print(start())
