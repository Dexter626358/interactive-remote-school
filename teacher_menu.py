from group_data_provider import show_groupmates as sg
from start import open_data_user as od
test_list = od('data_users.txt')


def teacher_menu(name_surname):
    global list_data
    print(f'{name_surname}, добро пожаловать в меню преподавателя!')
    print('1. Посмотреть список студентов')
    print('2. Успеваемость студентов')
    print('3. Расписание студентов')
    print('4. Просмотр и редактирование ДЗ')
    teacher_click = input("\nВведите нужный пункт: ")
    if teacher_click == '1':
        searchable_group = input("Введите номер группы: ")
        print()
        sg(test_list, searchable_group)
    elif teacher_click == '2':
        pass
    elif teacher_click == '3':
        pass
    elif teacher_click == '4':
        pass



teacher_menu("Мария Николаевна")