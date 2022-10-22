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
            elif day and not groupe:
                if i[keys2] == day:
                    print(f'{key} : {value}')
            elif groupe and not day:
                if i[keys1] == groupe:
                    print(f'{key} : {value}')
        print()
    print()
    if groupe and day:
        log(f'посмотрел базу "расписание" на {day} для группы {groupe}.')
        yellow(f'Отображено расписание на {day} для группы {groupe} ')
    elif groupe and not day:
        log(f'посмотрел базу "расписание" для группы {groupe}.')
        yellow(f'Отображено расписание на сентябрь для группы {groupe} ')
    elif day and not groupe:
        log(f'посмотрел базу "расписание" на {day}.')
        yellow(f'Отображено расписание на {day} ')
    white('')