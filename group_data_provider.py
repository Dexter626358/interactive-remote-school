from data_file import open_data_user as od
path = 'data_users.txt'
test_list = od(path)


def show_groupmates(data: list, group):
    result_lst = []
    print(f'Список студентов {group} группы:\n')
    for i in data:
        if i[7] == group:
            result_lst.append(i)
    for j in result_lst:
        print(j[2], j[3], j[4])
    print("\nСписок студентов успешно выгружен!")


def show_and_find_student(data: list, group):
    result_lst = []
    for i in data:
        if i[7] == group:
            result_lst.append(i)
    for j in result_lst:
        print(j)
    print("\nВыберите студента введя его ID ( 1-ое значение в списке )")
    chosen_student = input("Введите ID: ")
    return chosen_student



