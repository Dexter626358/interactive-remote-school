from start import open_data_user as od
path = 'data_users.txt'
test_list = od(path)


def show_groupmates(data: list, group):
    result_lst = []
    for i in data:
        if i[7] == group:
            result_lst.append(i)
    user_return = int(input("1 - возврат списка\n2 - возврат строки\nВведите нужное: "))
    if user_return == 1:
        for i in result_lst:
            print(i)
        return result_lst
    elif user_return == 2:
        for i in result_lst:
            print(i[2], i[3], i[4])



show_groupmates(test_list, '10')
