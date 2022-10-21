# Данный блок выводит на экран текущую базу данных.


from color_out_text import out_white as white
from color_out_text import out_yellow as yellow
from logger_action import logger_action as log


def view_schedule(dict_list_: list, groupe = None, day = None):
    keys1 = 'группа'
    keys2 = 'день'
    for i in dict_list_:
        for key, value in i.items():
            if groupe and day:
                if i[keys1] == groupe and i[keys2] == day:
                    print(f'{key} : {value}')
            elif day:
                if i[keys2] == day:
                    print(f'{key} : {value}')
            elif groupe:
                if i[keys1] == groupe:
                    print(f'{key} : {value}')
        print()
    if groupe and day:
        log(f'посмотрел базу "расписание" на {day} для группы {groupe}.')
    if groupe:
        log(f'посмотрел базу "расписание" для группы {groupe}.')
    if day:
        log(f'посмотрел базу "расписание" на {day}.')
    yellow('Отображено текущее состояние базы.')
    white('')