# используется для сортировки
import operator
from operator import itemgetter


class Building:
    """Дом+информация о владельце"""

    def __init__(self, id, fio, floors, str_id):
        self.id = id
        self.fio = fio
        self.floors = floors
        self.str_id = str_id


class Street:
    """Улица"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class BStr:
    """
    'Дом-улица' для реализации
    связи многие-ко-многим
    """

    def __init__(self, str_id, bld_id):
        self.str_id = str_id
        self.bld_id = bld_id


# Улицы
strts = [
    Street(1, 'Артиллерийская улица'),
    Street(2, '2-я Бауманская улица'),
    Street(3, 'Алая улица'),

    Street(11, 'Проспект Победы'),
    Street(22, 'Проспект Ленина'),
    Street(33, 'Ладожская улица'),
]

# Владельцы домов
blds = [
    Building(1, 'Артамонов', 5, 1),
    Building(2, 'Петров', 8, 2),
    Building(3, 'Иваненко', 12, 3),
    Building(4, 'Иванов', 8, 3),
    Building(5, 'Иванин', 5, 3),
]

blds_strts = [
    BStr(1, 1),
    BStr(2, 2),
    BStr(3, 3),
    BStr(3, 4),
    BStr(3, 5),

    BStr(11, 1),
    BStr(22, 2),
    BStr(33, 3),
    BStr(33, 4),
    BStr(33, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(e.fio, e.floors, d.name)
                   for d in strts
                   for e in blds
                   if e.str_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.str_id, ed.bld_id)
                         for d in strts
                         for ed in blds_strts
                         if d.id == ed.str_id]

    many_to_many = [(e.fio, dep_name)
                    for dep_name, dep_id, emp_id in many_to_many_temp
                    for e in blds if e.id == emp_id]

    print('Задание А1')
    for d in strts:
        if (d.name[0]=='А'):
            print(d.name, ':')
            for i in blds:
                if i.str_id==d.id:
                    print(i.fio)

    print('\nЗадание А2')
    res_12_unsorted = []
    for d in strts:
        d_emps = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_emps) > 0:
            d_sals = [sal for _, sal, _ in d_emps]
            # Самое высокое здание - максимальное количество этажей на улице
            d_sals_max = max(d_sals)
            res_12_unsorted.append((d.name, d_sals_max))
    # Сортировка по количеству этвжей
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)



    print('\nЗадание А3')
    res_11 = sorted(many_to_many, key=itemgetter(1))
    print(res_11)



if __name__ == '__main__':
    main()
