# Данный блок выводит на экран текущую базу данных.


from color_out_text import out_white as white
from color_out_text import out_yellow as yellow
from logger_action import logger_action as log


def view_schedule(dict_list_: list, groupe = None, day = None):
    keys1 = 'группа'
    keys2 = 'день'
    keys3 = 'количество_уроков'
    if day == '31.09.2022':
        yellow('В сентябре всего 30 дней.')
        white('')
    else:
        for i in dict_list_:
            for key, value in i.items():
                if groupe and day:
                    if i[keys1] == groupe and i[keys2] == day:
                        if i[keys3] != '0':
                            print(f'{key} : {value}')
                        else:
                            print('\nЭто выходной день, учебы нет.')
                            break
                    else:
                        break
                elif day and not groupe:
                    if i[keys2] == day:
                        if i[keys3] != '0':
                            print(f'{key} : {value}')
                        else:
                            print('\nЭто выходной день, учебы нет.')
                            break
                    else:
                        break
                elif groupe and not day:
                    if i[keys1] == groupe:
                        if i[keys3] != '0':
                            print(f'{key} : {value}')
                        else:
                            print('\nЭто выходной день, учебы нет.')
                            break
                    else:
                        break
            else:
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